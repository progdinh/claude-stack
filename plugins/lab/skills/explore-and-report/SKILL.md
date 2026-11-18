---
name: explore-and-report
description: Research something external — an architecture, technique, library, toolchain, hardware part, dataset, protocol, or paper — and file a sourced, structured report (what it is, ups, downs scoped to this project's constraints, what to experiment with) plus an index row. Use whenever something new gets investigated, to check whether a derived idea already exists, or (survey mode) to rank the current best methods for a task on this project's own metric; the conclusion must not live only in chat scrollback. Generic version — if the project has its own skill named explore-and-report, use that one instead.
argument-hint: <the thing to explore> [--depth scan|read|deep] [--survey]
metadata:
  group: know
  phrase: "Research something external and file a sourced report: what it is, ups and downs in your units, what to try."
---

# Explore and report

**Topic:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults: explorations in docs/lab/explorations/ with a README.md index, ledger docs/lab/open.md; currencies = time, money, memory, bytes moved, energy, plus this project's own outcome metric. Say in one line that defaults are in use and that /lab:init would fix it."`

Working contract: [contract.md](../../reference/contract.md). The point is a
durable, checkable record instead of a conclusion nobody can trace back to
anything.

## Process

1. **Find a verifiable primary source.** A paper (arXiv / IEEE / ACM /
   proceedings), official vendor or project docs, a datasheet, an RFC/spec, or
   a maintained reference implementation. Use web search/fetch to find and
   confirm the actual URL — never write a citation from memory without
   checking it resolves. If no solid primary source exists (a forum trick, an
   unsourced marketing number), **say that explicitly** instead of dressing it
   up as one.
2. **Read to a declared depth, and say which** in the Status line:
   - `--depth scan` — abstract + figures + conclusion. Orientation only; never
     enough to adopt, reject, or call anything novel.
   - `--depth read` (default) — method and results sections. Extract: **the
     one number that matters** and its metric; **what it was measured on**
     (scale, data, hardware, seeds, baselines); the **ablation that shows
     which part carries the result**; and **what it does NOT show** —
     especially anything resembling this project's conditions.
   - `--depth deep` — plus appendices, the released code, and at least one
     number re-derived or re-run. Required before a decision rests on it.
   Read enough to explain it accurately, not to name-drop it. If code in this project already implements or
   tests it, reference the specific file/function.
3. **Write the report** with the template below.
4. **File it**: `<explorations dir>/<slug>.md`, kebab-case, named after the
   thing explored. Create the directory if missing.
5. **Update the index** `<explorations dir>/README.md` — one row
   (Date / Topic / Source / Status). Don't let the index drift from the
   folder. Keep a "Still to file" table there for sources raised but not yet
   written up.
6. **Append priced follow-ups** from "What to experiment with" to the
   open-questions ledger.

## Report template

```markdown
# <Name of the thing explored>

**Explored:** <YYYY-MM-DD>
**Source:** [<title>](<verified URL>) — <paper / official docs / datasheet /
reference implementation>
**Status:** <depth read + outcome, e.g. "read only, not implemented" /
"prototyped in src/x.py" / "rejected — see Downs" / "shallow scan, abstracts only">

## Architecture / technique
What it actually is and how it works — specific enough that someone could
reimplement the core idea from this section alone. Real shapes, operations,
resources, numbers; not the marketing name. ASCII/mermaid diagrams where they
clarify structure.

## Ups
Concrete advantages, quantified where possible, and specifically relevant to
*this* project's constraints — not praise copied from the abstract.

## Downs
Concrete costs or risks, same standard. If something is well-regarded in
general but a bad fit for these constraints, say so plainly.

## What to experiment with
Concrete, actionable next steps, each with a price — a specific config to
benchmark, a specific ablation, a section to implement. Not "explore further."
```

## Survey mode — when the topic is a *task*, not a named thing

"What is the best current way to do X" (`--survey`, or inferred when the
topic names a problem rather than a method, part or paper). The single-thing
template above cannot hold this; a survey squeezed into it comes out as a
shallow scan with no ranking. Same process, same hard rules, different body:

1. **Fix the ranking metric first, in this project's unit** (the profile's headline outcome metric and binding currency) —
   and the budget a contender must fit. A survey ranked on the papers' own
   headline metric answers somebody else's question.
2. **Log the search**: every query run, where, and how many results were
   opened. Stop rule: two consecutive queries that surface no new contender.
3. **One row per contender**, 4–10 rows, including the **boring baseline**
   (the thing a practitioner would do with no paper at all).
4. **Declare the depth per row** — scan / read / deep. A row at scan depth
   cannot be the pick.
5. **Two picks, kept separate**: best overall, and **best that fits our
   budget**. They are usually different, and the second is the result.
6. File as ``<explorations dir>/survey-<task>.md``; the index Status says `survey, N contenders, depth …`.
   The pick then gets its own single-thing report before any decision rests
   on it.

```markdown
# Survey: <task>

**Explored:** <YYYY-MM-DD>
**Ranking metric:** <metric, unit> · **Budget:** <the constraint a contender must fit>
**Status:** survey, <N> contenders, <k> read / <N-k> scanned

## Search log
| Query | Where | Opened | New contenders |
|---|---|---|---|

## Contenders
| Method | Source (verified URL) | Headline number (their metric) | Measured on (scale, data, hardware) | In our unit — measured / derived / assumed | Fits budget? | Depth |
|---|---|---|---|---|---|---|

## Picks
- **Best overall:** <method> — <why, one line>
- **Best that fits our budget:** <method> — <why, and by what margin it fits>
- **Boring baseline to beat:** <method + its number>

## What nobody has measured
The gap relevant to this project — conditions no row covers. (A claim that
the gap is *novel* is a separate job: `novelty-claim`.)

## What to experiment with
Priced next steps — normally: a single-thing report on the pick, then the
cheapest head-to-head against the baseline.
```

## Scope Ups/Downs to this project's currencies

A generic pros/cons list will miss what matters here. Walk the profile's
**Currencies** table and **House rules** and ask of each: does this thing help
or hurt it, and by how much? Typical misses:

- quoting a proxy (parameter count, benchmark score, stars) when the project's
  binding currency is something else (peak memory, bytes moved, p99, €/month);
- ignoring the **headline outcome metric** — if the thing affects it, say what
  it would do to *that*, never to the proxy;
- hardware or paid services without a **real price from a real supplier**, and
  what it displaces in the budget;
- portability: does it run on the project's actual target, or only on
  something bigger/newer/other-vendor?

## Hard rules

- **No fabricated or guessed URLs.** If you can't verify a source resolves,
  don't cite it. This rule is what makes the explorations folder worth
  anything.
- Things recalled from memory but not verified are labelled *recalled, not
  verified* and queued in "Still to file" — never cited as fact.
- **No matching track → don't file in the nearest neighbour quietly.** If the
  topic belongs to no existing track's stated question, say so up front and
  propose opening one (a new track folder with its own CLAUDE.md stating
  the one question it answers — the name and the question are theirs). Until they do, file in the nearest
  track with the index Status starting `**no matching track — filed here
  provisionally**`, and repeat that in the closing line. A track that merely
  *consumes* the finding is a neighbour, not a home.
- Every report gets filed **and indexed**.
- A scan that finds nothing is weak evidence of absence; say how many
  searches at what depth before anything is called novel.
- If the exploration changes a design choice, that's a **decision** — also
  run `lab:record-decision`. If the profile names an upstream it affects,
  record it there too.

End in the terminal with the four-part TL;DR (contract.md §5).
