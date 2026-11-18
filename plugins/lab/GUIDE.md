# lab — user guide

The README is for whoever maintains the plugin. This is for using it.

PDFs next to this file: **`lab-reference.pdf`** (the 21 lab commands, one line
each) and **`skills-reference.pdf`** (everything typeable on this machine:
personal, lab, repo-local, bundled, synced). Regenerate either with the
scripts in `reference/` after adding or changing skills.

## The idea in four lines

1. Every design choice is a hypothesis. Tie it to a **unit** or it's a habit.
2. Non-trivial work **starts with a plan and a challenge**, not with code.
3. Every step **ends in a file** (a derivation, report, decision, stage
   report) — never only in chat — and a four-part **TL;DR** in the terminal.
4. Every open question carries a **price**, and lives in a ledger.

`~/.claude/CLAUDE.md` makes Claude follow this in every project without being
asked; trivial work (bug fixes, one-liners, questions) is exempt.

## Start here, in a new project

```
/lab:init                      once — writes docs/lab/profile.md (metric, units, paths)
/lab:challenge-design <the least-justified number or choice in the repo>
```

Later, when a question belongs to no existing track of a multi-track repo:

```
/lab:new-track <folder> "<the one question it answers>"   rarely — opens the track, moves in misfiled records
```

## "I have a…" → which skill

| I have… | Type | You get |
|---|---|---|
| an idea I'm pitching — what would it take? | `/lab:prototype <idea> [--stage poc\|prototype\|mvp]` | one-page brief in ~10 min: riskiest assumption, smallest test, build/fake/skip, needs, effort, kill criteria |
| a vague theme, want directions | `/lab:draft-ideas <theme>` | ~12 ideas through forced lenses, culled, top 3 with first tests |
| a new problem, nothing built yet | `/lab:derive-ansatz <question>` | limits, an analogy with its breaking points, 2–4 candidate forms + kill tests |
| a paper/method I want to use here | `/lab:apply-academia <idea> on <target>` | gap to our budget in orders of magnitude; per-part verdict |
| something external to understand | `/lab:explore-and-report <thing> [--depth scan\|read\|deep]` | sourced report, ups/downs in *our* units |
| a *task*, and I want the best current method for it | `/lab:explore-and-report <task> --survey` | contenders ranked on *our* metric, search log, best-overall vs best-that-fits-budget |
| an existing choice I'm about to build on | `/lab:challenge-design <choice>` | survives / replaced / undecidable-without-measurement |
| a decision made (or reversed, or survived) | `/lab:record-decision <what>` | log entry incl. the wrong first attempt |
| a result | `/lab:repro-check` → `/lab:integrity-audit` (if from data) → `/lab:stage-report` | a number you can defend |
| docs / reports / code I no longer trust to be current | `/lab:stale [--docs] [--reports] [--code]` | what is no longer true, with evidence on both sides and a fix price; report-only |
| a result whose cause I'm assuming | `/lab:ablation-plan <effect>` | fewest runs that tell the explanations apart |
| an idea I think is new | `/lab:novelty-claim <idea>` | logged search, nearest neighbour, safe claim wording |
| something slow / too big / too costly | `/lab:perf-investigation <problem>` | where the cost really is; before → after |
| a rule, rubric, or reward function | `/lab:rule-stress-test <rule>` | cheapest exploit, who it favours, can it be enforced, patches |
| lost the thread on the **project** | `/lab:tldr` | state of play from the files, blocking item first |
| lost the thread on **what Claude just did** | `/last` | six-line digest of the last step, from the chat |
| a whole question, end to end | `/lab:run <question>` | picks the entry point and chains the above |

And, outside the plugin, for quick side questions:

```
/go                            resume whatever was interrupted — no questions ("sorry, misclick")
/go 2  ·  /go 1 3  ·  /go all  do item(s) of the last numbered list of next steps Claude proposed
/big-job [previous | name]     the multi-step job we left: its phase checklist with current states, remaining phases numbered
/where the pdf [--open]        the exact path of a thing, what it is, how to open it
/your-take idk                 undecided? Claude commits to a pick, says why and what would flip it; then /go 1
/progress [id]                 how far along a running job is, time left, finish clock (detail view)
/update-docs [--check]         regenerate SKILLS.md, the README table and both PDFs from the skills' frontmatter
/last                          six short blocks: asked, did, result, changed, open, next
/rectify <the correct fact>    Claude got something wrong: traces where the error spread, fixes it
/update-context "<new fact>"   something changed outside the session: what it invalidates, then records it
/last 3  ·  /last session      the last 3 exchanges · the whole conversation
/huh p99                       three lines: what it is, what it meant here
/huh that last line
```

## Time: ETAs, the status bar, and /progress

- Plans open with `ETA ~6 min (4–10) · done ≈ 14:32` — **Claude time**, as a
  clock time, re-issued whenever the plan changes. Estimates are corrected by a
  measured log (`~/.claude/eta-log.jsonl`); until it has ~5 entries they say
  *(uncalibrated)*.
- Three clocks, never mixed: **Claude time** (minutes) · **machine time** (a
  run's wall clock, ideally from a timed pilot) · **your / world time**.
- The **status bar** at the bottom of the terminal shows every logged plan and
  watched job live — `▓▓▓▓░░ 14/25 · ~6m left · ≈14:17` — refreshed every 5 s,
  with no command and no model turn. `/progress` is the detailed view (drift,
  stalls, unregistered jobs); being a skill, it queues behind a running turn —
  the bar doesn't. To remove the bar: delete `statusLine` from
  `~/.claude/settings.json` (a backup sits beside it).

## How /rectify and /update-context decide whether to ask

| Situation | What happens |
|---|---|
| Trivial — nothing derived from it, no decision moves | applied immediately, reported in one line |
| Consequential — a number, decision, file, or plan changes | impact list (old → new), then **always asks** before editing |
| Conflicts with solid evidence — looks like a slip | **flagged first** with the evidence and a "did you mean…"; nothing changes until you confirm |

Records are superseded, never erased: the old value stays, dated, pointing at
what replaced it.

## Typical flows

**New research direction**
`draft-ideas` → `derive-ansatz` on the top 2 → `novelty-claim` on the
survivor → `record-decision` (hypothesis promoted, kill test priced).

**"Saw a paper, want it in our system"**
`explore-and-report --depth read` → `apply-academia` → plan mode →
build the *scaled-down reproduction first* → `stage-report`.

**Before trusting / publishing a number**
`repro-check` → `integrity-audit` → `ablation-plan` (if the cause matters) →
`stage-report`.

**Designing a competition or a reward**
`derive-ansatz` on the format → `rule-stress-test` on every scoring clause →
`record-decision`.


## You don't have to type the slash commands

Except the four manual-only ones, `/lab:init` and `/lab:new-track`, Claude invokes these itself
when the request matches — "derive this from first principles", "is this
actually novel?", "why is this slow", "where are we". Typing the command just
guarantees which procedure runs.

## What lands where (defaults; `profile.md` can repoint any of them)

```
docs/lab/profile.md         the project's metric, units, paths, house rules
docs/lab/decisions.md       why — ends with "Open / not yet decided"
docs/lab/open.md            the ledger: item · price · raised by · status
docs/lab/ideas.md           draft-ideas output, kills included
docs/lab/derivations/       derive-ansatz, apply-academia   (+ README index)
docs/lab/explorations/      explore-and-report, novelty-claim (+ README index)
docs/lab/reports/           stage-report, ablation plans, integrity audits
docs/lab/rules/  bom/  partners/
```

## Reading a TL;DR

```
(Correction, if any — always first)
TL;DR      what happened, and the number
⚑ Flagged   what could make it wrong — assumed inputs, unmeasured-on-target
→ Implies   what it changes — names a file, stage, or hypothesis
? Deeper    what to study next — each with a price
```

If `⚑ Flagged` is empty or `? Deeper` has no prices, push back — that's the
contract being skipped.

## Tuning it

- A skill behaves oddly → edit its `SKILL.md`; changes are live.
- Too much ceremony in small projects → tighten the "Exempt" list in
  `~/.claude/CLAUDE.md`.
- A project needs different units or paths → edit its `docs/lab/profile.md`,
  not the skills.
- **"Unknown command: /lab:…"** → the session started before the plugin (or
  that skill) existed. Plugins load at session start: run `/reload-plugins`,
  or restart `claude`. Needed after adding a skill folder or editing
  `plugin.json` / `reference/`; *not* needed for edits to an existing
  `SKILL.md`. (Plain skills like `/huh` are picked up live — plugins aren't.)
- A skill aborts instantly with no output → its `!` injection line failed;
  keep those to plain `cat … || echo …` (see README, Decisions).
- Costs: on a Pro subscription these use time and usage quota, not money.
