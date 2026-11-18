---
name: integrity-audit
description: Audit a dataset, training/evaluation pipeline, backtest, or benchmark for the ways results become silently wrong — leakage between train and test, lookahead / time-travel, survivorship and selection bias, label or target contamination, tuning on the test set, unrealistic cost/latency/fill assumptions, and undocumented data provenance. Use before trusting or publishing any result that comes from data — ML evaluations, trading backtests, simulators scored against logged data, benchmark comparisons — or when a result looks too good. (For code vulnerabilities use the built-in security-review instead.)
argument-hint: <pipeline, dataset, backtest, or result to audit>
metadata:
  group: trust
  phrase: "Is the number measuring what it claims? Leakage, lookahead, survivorship, test-set tuning, flattering simulators."
---

# Integrity audit

**Under audit:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/. Say so in one line; suggest /lab:init."`

`lab:repro-check` asks "can this number be regenerated?". This asks the next
question: **"is the number measuring what it claims to?"** A perfectly
reproducible leak is still a leak.

## 1. Trace the data path, end to end
From raw source to the reported number: every filter, join, split,
normalisation, augmentation, cache. Read the code; don't trust the README.
Draw it as a short list of stages. Most integrity bugs live at a stage
boundary.

## 2. Provenance
Per dataset: where it came from, when, under what licence/terms, what
selected it (who decided what got recorded?), what was dropped and why, and
**what it cannot tell you**. Undocumented = finding.

## 3. The leak checklist — check each against the code, cite file:line

| Class | What to look for |
|---|---|
| **Split leakage** | same entity (user, episode, track, session, file, near-duplicate) on both sides; split done after augmentation/windowing; random split on time-series or grouped data |
| **Preprocessing leakage** | normalisation stats, vocab, PCA, feature selection, imputation fitted on all data before the split |
| **Lookahead / time travel** | any feature at time t computed from data > t: centred windows, future-filled values, restated/revised data, labels that peek, `shift` in the wrong direction, bar close used to trade that same bar |
| **Target contamination** | the label (or a near-copy) reachable from the inputs; IDs or filenames that encode the class; oracle state fed to the policy |
| **Selection / survivorship** | only winners, only surviving assets, only completed episodes, only the runs that didn't crash |
| **Test-set tuning** | hyperparameters, early stopping, thresholds, architecture, or *the decision to stop iterating* chosen on the reported split. Count how many times the test set has been looked at |
| **Baseline handicap** | baseline given less tuning, less compute, older data, or a different metric |
| **Simulator honesty** | zero latency, zero cost, infinite liquidity, perfect fills, no slippage/impact, no queue position, no sensor noise, no actuation delay — every idealisation that flatters the result |
| **Metric mismatch** | the reported metric is a proxy for the profile's outcome metric, and they can disagree |
| **Multiple comparisons** | N variants tried, best reported, N not stated |

## 4. Cheap empirical tripwires — run the ones that cost minutes
- **Shuffle the labels / permute time** → performance must collapse to chance.
- **Train on noise features** → must learn nothing.
- **Trivial baseline** (last value, majority class, do-nothing, buy-and-hold)
  → how much of the headline result does it already get?
- **Shift features one step later** → a large drop means the model was reading the future.
- **Add realistic cost/latency** → does the edge survive?
- **Too good to be true?** Check it twice as hard.

## 5. Verdict per finding
**Confirmed leak** (with file:line and the tripwire that showed it) /
**Plausible, untested** (with the test and its price) / **Clean**. Then one
overall line: what the result can and cannot be claimed to show *today*.

File as `<reports dir>/integrity-<slug>.md`; untested items → ledger with
prices; a confirmed leak invalidates downstream results — name them, and
record via `lab:record-decision` using the corrected-first-attempt convention.

## Guards
- Report, don't silently fix — the before/after numbers are the evidence.
- "No leak found" states which classes were checked and how; it is not "clean".
- Don't expand into a pipeline rewrite.

End with the four-part TL;DR. A confirmed leak goes first, above everything.
