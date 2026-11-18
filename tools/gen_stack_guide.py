#!/usr/bin/env python3
"""Build the single stack guide PDF (English + French) from the skills' own frontmatter.

  uv run --with reportlab python tools/gen_stack_guide.py

Reads   plugins/*/skills/*/SKILL.md   (name, argument-hint, metadata.group, metadata.phrase)
        tools/phrases_fr.json         (French phrase per skill — add one when you add a skill)
Writes  docs/stack-guide.en.pdf  docs/stack-guide.fr.pdf
Fonts are macOS system fonts (Arial Unicode); change F below on another OS.
"""
import json
import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape as esc

ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()
FAVOURITES = ["go", "huh", "last", "progress", "your-take", "init", "derive-ansatz", "draft-ideas", "challenge-design"]

T = {
    "en": {
        "title": "sevel-stack", "sub": "A Claude Code stack: a first-principles research process (lab) and one-word reflexes (reflexes)",
        "intro": "Every design choice is a hypothesis tied to a <b>unit</b>. Non-trivial work <b>starts with a plan and a challenge</b>. Every step "
                 "<b>ends in a file</b> and a four-part TL;DR. Every open question carries a <b>price</b>. The reflexes are short skills that read "
                 "the conversation and answer in a few lines.",
        "install": "Install", "fav": "The nine I use most", "fav_note": "Typical flow: draft-ideas &rarr; derive-ansatz &rarr; challenge-design. "
                   "The reflexes (go, huh, last, progress, your-take) work in any conversation, in any project.",
        "rest": "Everything else", "tldr_h": "How every step ends in the terminal",
        "tldr": "(Correction, if any &mdash; always first)<br/>TL;DR &nbsp;&nbsp;&nbsp;&nbsp; what happened, and the number<br/>"
                "! Flagged &nbsp; what could make it wrong: assumed inputs, anything not measured on the real target<br/>"
                "→ Implies &nbsp; what it changes: names a file, a stage, or a hypothesis<br/>"
                "? Deeper &nbsp;&nbsp; what to study next, each with a price",
        "tldr_note": "Every number is <b>measured</b>, <b>sourced</b>, <b>derived</b> or <b>assumed</b>, and says which.",
        "mix": "Easy to mix up: <b>/reflexes:go</b> gives the go-ahead to execute (bare, it resumes what was interrupted); <b>/big-job</b> is for when you "
               "diverted into many subtasks and need to recall what the big job was; <b>/rectify</b> corrects Claude's own output; "
               "<b>/update-context</b> records a change that touches the whole project (vault included); <b>/last</b> sums up the last prompt and its output; "
               "<b>/lab:tldr</b> summarises the project's files and the processes that produced them. <b>/lab:init</b> sets a project up; "
               "Claude Code's own /init writes a CLAUDE.md.",
        "bare": "Plugin skills are namespaced (/lab:tldr, /reflexes:go). Copy a skill folder to ~/.claude/skills/ to get the bare name (/go).",
        "groups": {"reflex": "Reflexes", "start": "Start", "idea": "When you have an idea", "know": "Knowing what exists", "decide": "Deciding",
                   "trust": "Trusting a result", "docs": "Keeping the docs current"},
        "footer": "generated", "args": "arguments",
    },
    "fr": {
        "title": "sevel-stack", "sub": "Une pile Claude Code : un processus de recherche par les premiers principes (lab) et des réflexes en un mot (reflexes)",
        "intro": "Tout choix de conception est une hypothèse reliée à une <b>unité</b>. Le travail non trivial <b>commence par un plan et une remise en cause</b>. "
                 "Chaque étape <b>se termine par un fichier</b> et un TL;DR en quatre parties. Chaque question ouverte porte un <b>prix</b>. Les réflexes sont "
                 "de courts skills qui lisent la conversation et répondent en quelques lignes.",
        "install": "Installation", "fav": "Les neuf que j'utilise le plus", "fav_note": "Enchaînement typique : draft-ideas &rarr; derive-ansatz &rarr; "
                   "challenge-design. Les réflexes (go, huh, last, progress, your-take) marchent dans n'importe quelle conversation, dans tout projet.",
        "rest": "Tout le reste", "tldr_h": "Comment chaque étape se termine dans le terminal",
        "tldr": "(Correction, s'il y en a &mdash; toujours en premier)<br/>TL;DR &nbsp;&nbsp;&nbsp;&nbsp; ce qui s'est passé, et le chiffre<br/>"
                "! Signalé &nbsp; ce qui pourrait le rendre faux : entrées supposées, tout ce qui n'est pas mesuré sur la vraie cible<br/>"
                "→ Implique &nbsp; ce que cela change : nomme un fichier, une étape ou une hypothèse<br/>"
                "? Creuser &nbsp;&nbsp; quoi étudier ensuite, chacun avec un prix",
        "tldr_note": "Chaque chiffre est <b>mesuré</b>, <b>sourcé</b>, <b>dérivé</b> ou <b>supposé</b>, et le dit.",
        "mix": "Faciles à confondre : <b>/go</b> donne le feu vert pour exécuter (seul, il reprend ce qui a été interrompu) ; <b>/big-job</b> sert quand on "
               "a dévié dans plein de sous-tâches et qu'on veut retrouver le grand chantier ; <b>/rectify</b> corrige une sortie de Claude ; "
               "<b>/update-context</b> enregistre un changement qui touche tout le projet (coffre compris) ; <b>/last</b> résume le dernier prompt et sa réponse ; "
               "<b>/lab:tldr</b> résume les fichiers du projet et les processus qui les ont produits. <b>/lab:init</b> installe la méthode dans un projet ; "
               "le /init de Claude Code écrit un CLAUDE.md.",
        "bare": "Les skills de plugin ont un espace de noms (/lab:tldr, /reflexes:go). Copiez le dossier d'un skill dans ~/.claude/skills/ pour avoir le nom court (/go).",
        "groups": {"reflex": "Réflexes", "start": "Démarrer", "idea": "Quand on a une idée", "know": "Savoir ce qui existe", "decide": "Décider",
                   "trust": "Se fier à un résultat", "docs": "Garder la doc à jour"},
        "footer": "généré le", "args": "arguments",
    },
}
GROUP_ORDER = ["start", "idea", "know", "decide", "trust", "reflex", "docs"]


def frontmatter(path):
    text = path.read_text()
    block = text[4:text.index("\n---\n", 4)]
    out, section = {}, None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and section:
            k, _, v = line.strip().partition(":")
            out[section][k.strip()] = v.strip().strip('"')
        else:
            k, _, v = line.partition(":")
            v = v.strip()
            if v == "":
                section = k.strip()
                out[section] = {}
            else:
                section = None
                out[k.strip()] = v.strip('"') if not v.startswith('"<') else v
    return out


def collect():
    rows = {}
    for plugin in ("lab", "reflexes"):
        for f in sorted((ROOT / "plugins" / plugin / "skills").glob("*/SKILL.md")):
            fm = frontmatter(f)
            meta = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
            name = fm.get("name") or f.parent.name
            rows[name] = {"name": name, "cmd": f"/{plugin}:{name}", "hint": fm.get("argument-hint", ""),
                          "group": meta.get("group", ""), "en": meta.get("phrase", "")}
    return rows


def build(lang, rows, fr):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    t = T[lang]
    F = "/System/Library/Fonts/Supplemental/"
    pdfmetrics.registerFont(TTFont("U", F + "Arial Unicode.ttf"))
    pdfmetrics.registerFont(TTFont("B", F + "Arial Bold.ttf"))
    pdfmetrics.registerFont(TTFont("M", F + "Courier New Bold.ttf"))
    registerFontFamily("U", normal="U", bold="B", italic="U", boldItalic="B")
    INK, MUTED = colors.HexColor("#1d1b18"), colors.HexColor("#6b655c")
    RULE, ACCENT, BAND = colors.HexColor("#d9d2c5"), colors.HexColor("#a5481f"), colors.HexColor("#f4efe6")

    def st(name, **kw):
        base = dict(fontName="U", fontSize=9, leading=12.2, textColor=INK)
        base.update(kw)
        return ParagraphStyle(name, **base)

    S = {"title": st("t", fontName="B", fontSize=22, leading=26), "sub": st("s", fontSize=10, leading=14, textColor=MUTED),
         "h": st("h", fontName="B", fontSize=11.5, leading=15, textColor=ACCENT, spaceBefore=9, spaceAfter=1, keepWithNext=1),
         "p": st("p"), "small": st("sm", fontSize=8, leading=10.5, textColor=MUTED),
         "cmd": st("c", fontName="M", fontSize=8.2, leading=11), "what": st("wh", fontSize=8.7, leading=11.4),
         "mono": st("m", fontName="M", fontSize=8, leading=10.8)}
    P = lambda x, s="p": Paragraph(x, S[s])

    def phrase(r):
        return esc(fr[r["name"]] if lang == "fr" else r["en"])

    def pairs(members):
        out = []
        for r in members:
            what = phrase(r)
            if r["hint"]:
                what += f"<br/><font name='M' size='7.6' color='#6b655c'>{esc(r['hint'])}</font>"
            out.append((esc(r["cmd"]), what))
        return out

    def table(pp):
        tb = Table([[P(c, "cmd"), P(w, "what")] for c, w in pp], colWidths=(52 * mm, 122 * mm), hAlign="LEFT")
        tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE),
                                ("TOPPADDING", (0, 0), (-1, -1), 2.8), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.8),
                                ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]))
        return tb

    def band(text, style="mono"):
        tb = Table([[P(text, style)]], colWidths=[174 * mm])
        tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), BAND), ("LEFTPADDING", (0, 0), (-1, -1), 7),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 6),
                                ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
        return tb

    fav = [rows[n] for n in FAVOURITES]
    rest = [r for r in rows.values() if r["name"] not in FAVOURITES]
    story = [P(t["title"], "title"), P(t["sub"], "sub"), Spacer(1, 7), P(t["intro"]), Spacer(1, 6),
             P(t["install"], "h"), Spacer(1, 2),
             band("/plugin marketplace add progdinh/claude-stack<br/>/plugin install lab@sevel-stack<br/>/plugin install reflexes@sevel-stack"),
             Spacer(1, 3), P(t["bare"], "small"),
             KeepTogether([P(t["fav"], "h"), Spacer(1, 2), table(pairs(fav)), Spacer(1, 2), P(t["fav_note"], "small")])]
    story.append(P(t["rest"], "h"))
    for g in GROUP_ORDER:
        members = [r for r in rest if r["group"] == g]
        if members:
            story.append(KeepTogether([P(f"<b>{t['groups'][g]}</b>", "p"), Spacer(1, 1), table(pairs(members)), Spacer(1, 5)]))
    story += [KeepTogether([P(t["tldr_h"], "h"), Spacer(1, 2), band(t["tldr"]), Spacer(1, 3), P(t["tldr_note"], "small")]),
              Spacer(1, 6), P(t["mix"], "small")]

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("U", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 10 * mm, f"sevel-stack · {t['footer']} {TODAY}")
        canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, str(doc.page))
        canvas.restoreState()

    out = ROOT / "docs" / f"stack-guide.{lang}.pdf"
    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=17 * mm,
                      title="sevel-stack", author="Joseph Giordano-Dinh (SEVEL LABS)").build(story, onFirstPage=footer, onLaterPages=footer)
    return out


if __name__ == "__main__":
    rows = collect()
    fr = json.loads((Path(__file__).parent / "phrases_fr.json").read_text())
    missing = [n for n, r in rows.items() if n not in fr or not r["en"] or r["group"] not in T["en"]["groups"]]
    if missing:
        sys.exit(f"missing French phrase / English phrase / known group for: {missing}")
    for lang in ("en", "fr"):
        print("wrote", build(lang, rows, fr))
