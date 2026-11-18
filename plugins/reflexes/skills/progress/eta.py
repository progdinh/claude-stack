#!/usr/bin/env python3
"""Tiny ETA calibration log — makes "Claude time" a measured thing instead of a guess.

  eta.py now                                  the clock (Claude cannot perceive time; ask)
  eta.py clock <seconds>                      when something taking <seconds> from now would finish
  eta.py start "<label>" <est_seconds> [kind] [--out FILE --total N --pattern REGEX]
                                              open an entry; with --out/--total/--pattern the status
                                              line counts matching lines in FILE live (k/N), no model turn
  eta.py status                               ONE line for the Claude Code status bar (reads its JSON on stdin)
  eta.py end <id> [note]                      close it; prints actual vs estimate
  eta.py stats [substring|kind]               how wrong past estimates were -> correction factor
  eta.py rate <done> <total> <elapsed_s>      progress maths: percent, rate, remaining, finish clock

kind: plan | shell | agent | skill | edit | other        Log: ~/.claude/eta-log.jsonl
"""
import json
import statistics
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

LOG = Path.home() / ".claude" / "eta-log.jsonl"


def fmt(s: float) -> str:
    s = int(round(s))
    if s < 90:
        return f"{s}s"
    m, sec = divmod(s, 60)
    if m < 90:
        return f"{m}m{sec:02d}s" if m < 10 else f"{m}m"
    h, m = divmod(m, 60)
    return f"{h}h{m:02d}m"


def clock(seconds_from_now: float) -> str:
    t = datetime.now() + timedelta(seconds=seconds_from_now)
    day = "" if t.date() == datetime.now().date() else t.strftime(" %a")
    return t.strftime("%H:%M") + day


def rows():
    if not LOG.exists():
        return []
    return [json.loads(line) for line in LOG.read_text().splitlines() if line.strip()]


def write(all_rows):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in all_rows))


def status_line() -> str:
    """One line for the status bar. Must be fast and must never raise."""
    import re
    head = ""
    try:
        if not sys.stdin.isatty():
            d = json.loads(sys.stdin.read() or "{}")
            model = (d.get("model") or {}).get("display_name", "")
            cwd = Path((d.get("workspace") or {}).get("current_dir", "") or ".").name
            pct = (d.get("context_window") or {}).get("used_percentage")
            head = " · ".join(x for x in (model, cwd, f"ctx {pct:.0f}%" if isinstance(pct, (int, float)) else "") if x)
    except Exception:
        pass
    parts = []
    try:
        live = [r for r in rows() if "actual_s" not in r and time.time() - r["t0"] < 12 * 3600]
        for r in live[-2:]:
            el = time.time() - r["t0"]
            label = r["label"][:34]
            w = r.get("watch")
            if w:
                try:
                    txt = Path(w["out"]).read_text(errors="ignore")
                    k = len(re.findall(w["pattern"], txt, flags=re.M))
                    # the job usually started before it was registered: time it from
                    # the output file's creation, not from the registration
                    st = Path(w["out"]).stat()
                    born = getattr(st, "st_birthtime", None) or r["t0"]
                    el = time.time() - min(born, r["t0"])
                except Exception:
                    k = 0
                n = w["total"]
                if k >= n:
                    parts.append(f"✔ {label} {int(k)}/{int(n)} in {fmt(el)}")
                elif k > 0:
                    rem = (n - k) * el / k
                    bar = "▓" * int(10 * k / n) + "░" * (10 - int(10 * k / n))
                    parts.append(f"{bar} {int(k)}/{int(n)} {label} · ~{fmt(rem)} left · ≈{clock(rem)}")
                else:
                    parts.append(f"░░░░░░░░░░ 0/{int(n)} {label} · {fmt(el)} elapsed")
            else:
                rem = r["est_s"] - el
                tail = f"~{fmt(rem)} left · ≈{clock(rem)}" if rem > 0 else f"+{fmt(-rem)} over est"
                parts.append(f"⏱ {label} · {fmt(el)}/{fmt(r['est_s'])} · {tail}")
        if len(live) > 2:
            parts.append(f"(+{len(live) - 2} more)")
    except Exception:
        pass
    return "  │  ".join(x for x in [head] + parts if x) or " "


def main(a):
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd = a[0]

    if cmd == "now":
        print(datetime.now().strftime("%H:%M:%S %a %Y-%m-%d"), int(time.time()))

    elif cmd == "clock":
        print(f"{fmt(float(a[1]))} from now -> done ≈ {clock(float(a[1]))}")

    elif cmd == "start":
        label, est = a[1], float(a[2])
        rest, watch = a[3:], {}
        for flag in ("--out", "--total", "--pattern"):
            if flag in rest:
                i = rest.index(flag)
                watch[flag[2:]] = rest[i + 1]
                del rest[i:i + 2]
        kind = rest[0] if rest else "other"
        rs = rows()
        rid = f"e{len(rs) + 1}"
        entry = {"id": rid, "label": label, "kind": kind, "est_s": est, "t0": time.time(),
                 "started": datetime.now().isoformat(timespec="seconds")}
        if watch.get("out") and watch.get("total"):
            entry["watch"] = {"out": watch["out"], "total": float(watch["total"]),
                              "pattern": watch.get("pattern", ".")}
        rs.append(entry)
        write(rs)
        print(f"{rid} started {datetime.now():%H:%M:%S} · est {fmt(est)} · done ≈ {clock(est)}")

    elif cmd == "end":
        rs = rows()
        for r in rs:
            if r["id"] == a[1] and "actual_s" not in r:
                r["actual_s"] = round(time.time() - r["t0"], 1)
                w = r.get("watch")
                if w:  # a watched job is timed by its output file, not by when the entry got closed
                    try:
                        st = Path(w["out"]).stat()
                        born = getattr(st, "st_birthtime", None) or r["t0"]
                        r["actual_s"] = round(st.st_mtime - min(born, r["t0"]), 1)
                    except Exception:
                        pass
                r["ratio"] = round(r["actual_s"] / r["est_s"], 2) if r["est_s"] else None
                if len(a) > 2:
                    r["note"] = " ".join(a[2:])
                write(rs)
                verdict = "on target" if 0.7 <= r["ratio"] <= 1.4 else ("UNDER-estimated" if r["ratio"] > 1.4 else "OVER-estimated")
                print(f"{r['id']} {r['label']}: est {fmt(r['est_s'])} · actual {fmt(r['actual_s'])} · x{r['ratio']} ({verdict})")
                return 0
        print(f"no open entry {a[1]}")
        return 1

    elif cmd == "status":
        print(status_line())

    elif cmd == "stats":
        key = a[1].lower() if len(a) > 1 else ""
        done = [r for r in rows() if "ratio" in r and r["ratio"]
                and (not key or key in r["label"].lower() or key == r["kind"])]
        if not done:
            print(f"no closed entries{' matching ' + key if key else ''} — estimates are UNCALIBRATED; say so.")
            return 0
        ratios = sorted(r["ratio"] for r in done)
        med = statistics.median(ratios)
        lo, hi = ratios[int(0.1 * (len(ratios) - 1))], ratios[int(round(0.9 * (len(ratios) - 1)))]
        print(f"n={len(done)} · actual/estimate median x{med:.2f} (p10 x{lo:.2f}, p90 x{hi:.2f})")
        print(f"-> multiply a gut estimate by {med:.2f}; give the range x{lo:.2f}..x{hi:.2f}"
              + ("" if len(done) >= 5 else "   [n<5: weak — still say 'uncalibrated']"))
        for r in done[-8:]:
            print(f"   {r['kind']:<6} est {fmt(r['est_s']):>7} actual {fmt(r['actual_s']):>7} x{r['ratio']:<5} {r['label'][:60]}")

    elif cmd == "rate":
        done_n, total, elapsed = float(a[1]), float(a[2]), float(a[3])
        if done_n <= 0:
            print(f"0/{int(total)} after {fmt(elapsed)} — no rate yet; cannot estimate.")
            return 0
        per = elapsed / done_n
        rem = (total - done_n) * per
        pct = 100 * done_n / total
        bar = "█" * int(pct // 5) + "░" * (20 - int(pct // 5))
        print(f"{bar} {pct:.0f}% · {int(done_n)}/{int(total)} · elapsed {fmt(elapsed)} · {fmt(per)}/item"
              f" · remaining ~{fmt(rem)} · done ≈ {clock(rem)}")
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
