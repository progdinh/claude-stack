#!/usr/bin/env python3
"""Mechanical staleness scan. Report-only; never edits anything.

  stale_scan.py [root] [--docs] [--code] [--max N]

--docs  dead references (a doc cites a path that no longer exists) and
        overtaken docs (a cited file changed in git AFTER the doc last did)
--code  Python imports not declared in the nearest pyproject.toml
Default: both. Judgement-type staleness (a conclusion overtaken by a later
decision, a status row that lies) is NOT detectable here — the skill does that.
"""
import ast
import re
import subprocess
import sys
from pathlib import Path

SKIP = {".git", "node_modules", ".venv", "venv", "__pycache__", "artifacts", "dist", "build", ".mypy_cache", ".pytest_cache"}
REF = re.compile(r"`([^`\s]+)`")
EXT = (".py", ".md", ".json", ".toml", ".yaml", ".yml", ".sh", ".ts", ".js", ".rs", ".v", ".sv", ".ipynb", ".txt", ".csv", ".html")


def walk(root, suffixes):
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in suffixes and not (set(p.parts) & SKIP):
            yield p


def git_time(path, root):
    try:
        out = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%ct", "--", str(path)],
                             capture_output=True, text=True, timeout=10).stdout.strip()
        return int(out) if out else None
    except Exception:
        return None


def looks_like_path(tok):
    if any(c in tok for c in "<>*{}$|()=,;") or tok.startswith(("http", "-", "/lab:", "#")):
        return False
    tok = tok.rstrip("/.:")
    if not re.fullmatch(r"[\w.\-/~]+", tok) or not re.search(r"[A-Za-z]{2}", tok):
        return False
    return ("/" in tok and not tok.startswith("/") and len(tok) > 3 and not tok.replace("/", "").isdigit()) or tok.endswith(EXT)


def scan_docs(root, cap):
    dead, overtaken = [], []
    names = {}
    for f in root.rglob("*"):
        if not (set(f.parts) & SKIP):
            names.setdefault(f.name, f)
    for doc in walk(root, {".md"}):
        text = doc.read_text(errors="ignore")
        dt = None
        seen = set()
        for m in REF.finditer(text):
            tok = m.group(1).rstrip("/.:,")
            tok = tok.split(":")[0] if re.search(r":\d+$", m.group(1)) else tok
            if tok in seen or not looks_like_path(tok):
                continue
            seen.add(tok)
            cands = [doc.parent / tok, root / tok] + [a / tok for a in doc.parents if root in a.parents or a == root]
            hit = next((c for c in cands if c.exists()), None)
            if hit is None and "/" not in tok:
                hit = names.get(tok)          # bare filename that lives somewhere in the repo
            if hit is None and (root.parent / tok).exists():
                continue                      # a sibling repo, e.g. AGP/... — out of scope
            line = text[:m.start()].count("\n") + 1
            if hit is None:
                if tok.startswith(("~", "..")) or tok.split("/")[0] in ("docs", "artifacts") and "lab" in tok:
                    continue
                dead.append((doc.relative_to(root), line, tok))
            elif hit.is_file() and hit.suffix != ".md":
                dt = dt if dt is not None else (git_time(doc, root) or 0)
                ft = git_time(hit, root)
                if dt and ft and ft - dt > 86400:
                    overtaken.append((doc.relative_to(root), hit.relative_to(root), (ft - dt) // 86400))
    return dead[:cap], len(dead), overtaken[:cap], len(overtaken)


def scan_code(root, cap):
    std = set(getattr(sys, "stdlib_module_names", ()))
    out = []
    for proj in [p.parent for p in walk(root, {".toml"}) if p.name == "pyproject.toml"]:
        decl = (proj / "pyproject.toml").read_text(errors="ignore").lower()
        local = {p.stem for p in proj.iterdir()} | {p.name for p in proj.iterdir() if p.is_dir()}
        for sib in root.iterdir():            # packages reached via sys.path hacks into sibling tracks
            if sib.is_dir() and sib.name not in SKIP:
                local |= {q.name for q in sib.iterdir() if q.is_dir()} | {q.stem for q in sib.glob("*.py")}
        used = {}
        for py in walk(proj, {".py"}):
            try:
                tree = ast.parse(py.read_text(errors="ignore"))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                mods = [a.name for a in node.names] if isinstance(node, ast.Import) else \
                       [node.module] if isinstance(node, ast.ImportFrom) and node.module and node.level == 0 else []
                for m in mods:
                    used.setdefault(m.split(".")[0], py.relative_to(root))
        for mod, where in sorted(used.items()):
            alias = {"cv2": "opencv", "PIL": "pillow", "yaml": "pyyaml", "sklearn": "scikit-learn"}.get(mod, mod).lower()
            if mod in std or mod in local or mod.startswith("_") or alias in decl or alias.replace("_", "-") in decl:
                continue
            out.append((proj.relative_to(root) if proj != root else Path("."), mod, where))
    return out[:cap], len(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    cap = int(args[args.index("--max") + 1]) if "--max" in args else 25
    root = Path(next((a for a in args if not a.startswith("--") and not a.isdigit()), ".")).resolve()
    both = "--docs" not in args and "--code" not in args
    if both or "--docs" in args:
        dead, nd, over, no = scan_docs(root, cap)
        print(f"## dead references: {nd}")
        for d, l, t in dead:
            print(f"  {d}:{l}  cites `{t}` — not found")
        print(f"## docs overtaken by a file they cite: {no}")
        for d, f, days in sorted(over, key=lambda x: -x[2]):
            print(f"  {d}  <-  {f} changed {days}d later")
    if both or "--code" in args:
        und, nu = scan_code(root, cap)
        print(f"## imports not declared in pyproject: {nu}")
        for proj, mod, where in und:
            print(f"  [{proj}] import {mod}  (first seen {where})")
