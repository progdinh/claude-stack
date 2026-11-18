---
name: run
description: Take a question, idea, or design problem through the whole lab pipeline — pick the right entry stage (derive an ansatz when there is no incumbent, challenge when there is one, explore when it is about something external), chain the stages with files as the hand-off, and finish with recorded decisions, a priced ledger, and a terminal TL;DR. Use when asked to "work through", "think about from first principles", "figure out what we should do about" a problem end to end, rather than for a single stage.
argument-hint: [the question or idea]
metadata:
  group: start
  phrase: "Work a question end to end: picks the right entry point and chains the stages."
---

# Run the lab pipeline

**Question:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Defaults under docs/lab/ will be used. Say so in one line and suggest /lab:init — but do not block on it."`

Working contract: [contract.md](../../reference/contract.md).

```
(draft) ► derive ──► explore ──► challenge ──► record ──► (plan ► build ► stage-report) ──► tldr
 new         does it      does the       why,          only if the user
 problem     exist?       incumbent      filed         asks to build
             what's       survive?
             known?
```

## 0. Skill resolution

For every stage below: if the project has its **own** skill of that name
(e.g. a local `derive-ansatz`), invoke that one — it is the specialised
version. Otherwise invoke the `lab:` one.

## 1. Route — pick the entry stage, say which and why in one line

| The question is about… | Enter at |
|---|---|
| an idea being **proposed or pitched** — "what would this take", "poc/mvp for X" | **prototype** — a one-page brief; stop there unless asked to go on |
| a theme still **too vague to derive on** — "what could we try", "give me directions" | **draft-ideas**, then derive on the top two or three |
| a **proven idea from the literature** to bring into this project — "apply X to our Y" | **apply-academia** (runs explore first if no report on X exists) |
| a problem with **no incumbent** here — a new domain, task, objective, interface, "what should X even look like" | **derive-ansatz** |
| an **existing choice** — "is X right", "should we keep Y", a number with no derivation, about to build on top of something | **challenge-design** |
| something **external** — a paper, library, part, technique, "what's out there", "is this novel" | **explore-and-report** |
| a choice that has **already been made** in conversation and just isn't written down | **record-decision** |
| results that **already exist** and aren't written up | **stage-report** — after `repro-check`; and `integrity-audit` if the number comes from data |
| a result whose **cause is assumed** | **ablation-plan** |
| "is this **novel**" | **novelty-claim** |
| something is **slow / too big / too expensive** | **perf-investigation** |
| a **rule, rubric, or reward** someone will optimise against | **rule-stress-test** |
| "where are we" | **tldr** — and stop |

First check the decisions log and the derivations/explorations indexes: if
this question has already been through the pipeline, say so, summarise the
recorded answer, and only proceed if there is **new evidence**.

## 2. Chain — each stage reads the previous stage's *file*, not the chat

- **After derive:** hand the promoted and parked ansätze to **explore** — do
  they already exist, under what name, with what measured results? Update the
  derivation's verdicts if the literature kills or confirms one. Nothing is
  called novel before this step, and a shallow scan says it is shallow.
- **After explore:** if it bears on an existing choice, **challenge** that
  choice with the new evidence. If it bears on nothing yet, stop here.
- **After challenge:** **record** the verdict — including *survives*.
  "Undecidable without measurement" goes under `Open / not yet decided` with
  the measurement and its price.
- **Every stage** appends its priced open items to the ledger.

Stop the chain early when a stage's honest output is "needs a measurement".
More reasoning on top of an unmeasured premise is how wrong numbers get
confident. Say what the measurement is, what it costs, and stop.

## 3. Do not build

This pipeline ends at recorded decisions and priced tests. If the user wants
the thing built, that is a separate step that **starts in planning mode** with
the verdicts above as its inputs, and ends with `stage-report`.

## 4. Close — one TL;DR for the whole run, not one per stage

Four parts (contract.md §5). Corrections of anything said earlier go first.
`→ Implies` names files that changed. `? Deeper` is the ledger's cheapest
high-leverage items, each with its price. Finish with the list of files
written.

## Guards

- **One sitting.** If the run wants to go long, it is missing a measurement.
- **Don't skip stages silently.** If a stage is skipped, say why in one line
  ("no incumbent → challenge skipped").
- **Don't ask permission between stages** unless a stage surfaces a decision
  that is genuinely the user's (a rule, a budget, a scope change). Surface
  those as decisions-in-waiting and keep going on what doesn't depend on them.
