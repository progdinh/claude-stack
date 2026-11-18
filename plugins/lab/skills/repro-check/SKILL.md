---
name: repro-check
description: Before a result is cited, reported, or built upon, check that it can actually be reproduced from what is on disk — the exact command, the inputs, the seed, the environment, the code version — re-run it if cheap, and compare. Use when a number is about to go into a report, decision, paper, slide, or pitch; when picking up someone else's (or last month's) result; or when asked "can we trust this number". Produces a pass / partial / fail verdict with the specific missing piece.
argument-hint: <the result, report, or number to check>
metadata:
  group: trust
  phrase: "Can this number be regenerated from what is on disk? Command, code version, inputs, seed, environment."
---

# Reproducibility check

**Result under check:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/. Say so in one line; suggest /lab:init."`

A number that can't be regenerated is an anecdote. This takes minutes and is
cheapest the day the result is produced.

## Checklist — answer each from files, not memory

| # | Question | Pass condition |
|---|---|---|
| 1 | **Where is the number?** | It appears in a file on disk (artifact, log, CSV), not only in a report's prose or chat |
| 2 | **What command produced it?** | Exact command recorded, runnable from a clean checkout |
| 3 | **Which code?** | Commit hash recorded, or the tree is clean at a known commit; no uncommitted changes that affect it |
| 4 | **Which inputs?** | Data / config / checkpoint paths exist, are versioned or hashed, and aren't silently regenerated |
| 5 | **Which environment?** | Lockfile checked in and actually sufficient — try importing what the command needs |
| 6 | **Randomness?** | Seed fixed and recorded; or variance reported over n seeds |
| 7 | **How many runs?** | n stated. A single run is labelled as such |
| 8 | **Measured on what?** | The real target vs a simulator/model/estimate — labelled every time |
| 9 | **Constants consumed?** | Every assumed constant it depends on is listed with provenance |

## Then re-run it, if the price is small

State the price first (seconds, minutes, GPU-hours). If it's under a few
minutes, run it and compare to the recorded number:
- **Matches** within stated variance → pass.
- **Differs** → this is the finding. Report both numbers, bisect the cause
  (code drift, data drift, seed, environment) only as far as is cheap, and put
  the rest in the ledger with a price.
- **Won't run** → report the exact error. An environment that can't import
  its own dependencies is a fail on row 5, however good the number looks.

If the re-run is expensive, don't — say what it would cost and mark the
verdict *unverified by re-run*.

## Verdict — one of three, plus the single most important missing piece
- **Reproducible** — all rows pass (and re-run matched, if run).
- **Partially** — the number is probably right but row(s) N fail; name the fix
  and its price.
- **Not reproducible** — it cannot currently be regenerated. It must not be
  cited as a result until it can; say what to label it meanwhile (*estimate*,
  *single unrecorded run*).

Write the verdict into the report or decision that carries the number (a
`**Reproducibility:**` line), not into a separate file. Fails and partials go
in the ledger with a price.

## Guards
- Don't "fix" the result to make it match. Report the divergence.
- Don't extend the check into a refactor of the experiment code.
- A result that reproduces is not thereby *correct* — that's
  `lab:integrity-audit` (leakage, lookahead) and `lab:ablation-plan`
  (is it the cause you think it is).
