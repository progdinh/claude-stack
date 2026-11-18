---
name: stage-report
description: Close an implementation stage or experiment with a written report that carries measurements — the numbers in real units, which hypotheses were falsified or survived, what broke or was left undone, and what it unblocks or invalidates downstream — then update the roadmap and the open-questions ledger. Use when a stage, experiment, benchmark, or milestone has produced results, or when asked to "write up" / "report" what a piece of work found. Generic version — if the project has its own skill named stage-report, use that one instead.
argument-hint: [the stage or experiment that just finished]
metadata:
  group: trust
  phrase: "Close an experiment: the numbers, what was falsified, what broke, what it unblocks."
---

# Stage report

**Stage:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults: reports in docs/lab/reports/, raw outputs under artifacts/, roadmap docs/roadmap.md if present, ledger docs/lab/open.md. Say in one line that defaults are in use and that /lab:init would fix it."`

Working contract: [contract.md](../../reference/contract.md) §5. Planning
opens a step; a written record closes it. Nothing is done while its result
exists only in chat scrollback.

## The test for whether to write one at all

If the step produced **no measurement and falsified nothing**, say that in one
line in the terminal and stop — don't pad it into a document. A report whose
content is "these files were written" is not a report.

## Before writing

1. **Re-run or re-read the actual outputs.** Quote numbers from the artifacts,
   not from memory of the session. If a number can't be reproduced from a file
   on disk, it is not in the report.
2. **Find what the stage was supposed to test** — the roadmap row, the
   hypothesis (H-number), the plan's "what would falsify it". A report is
   written against that, not against what happened to get built.
3. **List every assumed constant the result consumed**, and where each came
   from. Assumptions compound across stages.

## Template — `<reports dir>/<sNN>-<slug>.md`

```markdown
# <Stage id — what it set out to establish>

**Date:** <YYYY-MM-DD>   **Artifacts:** <path to raw outputs>
**Reproduce:** `<the exact command>`

## Result
The headline number(s), in the profile's units, against the budget or
baseline they are judged by. One table. The outcome metric, never the proxy.

## What was falsified, what survived
Per hypothesis / expectation: the prediction, the measurement, the verdict.
A stage that confirms everything it expected usually wasn't testing anything —
if that is the case here, say so.

## What broke or was left undone
Stated plainly: known residuals, skipped cases, things that only work under a
condition, anything not measured on the real target. These belong in the
record so nobody assumes they went unnoticed.

## Provenance of inputs
| Input | Value | measured / sourced / derived / **assumed** | Used where |

## What this unblocks or invalidates
Name the downstream stage, hypothesis, decision entry, or file. If it changes
something in an upstream the profile names, say so — and record it there.

## Open questions raised
Each with a price.
```

## After writing

- Update the **roadmap** row's status, with the one-line result in it.
- Append the open questions to the **ledger**; close ledger items this stage
  answered (status → answered, with a pointer to this report).
- Any choice made or reversed along the way → `lab:record-decision`
  (including first attempts that were wrong — they are the valuable part).
- If a hypothesis died, mark it killed where live hypotheses are kept, with
  the number that killed it.
- If the profile has a `## Vault` section: write the report from the vault's
  analysis template (frontmatter `headline` with a number), add a row to
  Home's Analyses log, and update Home's Status table.

## Hard rules

- **Numbers carry units and provenance.** "Faster" is not a result.
- **Estimated ≠ measured.** A simulated or modelled figure for a real target
  is labelled as such every time it appears.
- **Corrections lead.** If this stage contradicts an earlier report or
  decision, that is the first line — and the earlier record gets a pointer to
  this one rather than a silent edit.
- Short. A stage report that needs scrolling three times is hiding its result.

End in the terminal with the four-part TL;DR (contract.md §5) — pointing at
what moved, not restating the file.
