---
name: ablation-plan
description: Given a result or an effect, design the smallest set of runs that discriminates between the competing explanations for it — list the rival explanations, what each predicts, and the few experiments whose outcomes differ between them, with a price per run and a stopping rule. Use when a result came out (good or bad) and the cause is assumed rather than shown, before claiming "X works because Y", before a paper/report attributes an improvement, or when asked what to run next.
argument-hint: <the result or effect to explain>
metadata:
  group: trust
  phrase: "The fewest runs that tell the competing explanations apart, predictions written down first."
---

# Ablation plan

**Effect to explain:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/ and generic currencies. Say so in one line; suggest /lab:init."`

Working contract: [contract.md](../../reference/contract.md). The goal is not
"ablate everything" — it is the **fewest runs whose outcomes would differ
depending on which explanation is true.**

## Procedure

### 1. State the effect, with its number and its noise
What changed, by how much, on the outcome metric, over how many seeds. If the
run-to-run variance is unknown, **measuring it is run zero** — no ablation is
interpretable without it. An effect smaller than the noise is not yet an
effect.

### 2. List the rival explanations — at least three, including the boring ones
The intended mechanism, plus: more parameters/compute/data, a changed
hyperparameter that rode along, a bug fixed in passing, a leak
(`lab:integrity-audit`), seed luck, an evaluation change, regression to the
mean, a confound in the comparison (different budget, different tuning
effort for the baseline).

### 3. Prediction table
Rows = explanations. Columns = candidate runs. Each cell: what that
explanation predicts for that run (↑ / ↓ / no change, roughly how much).
**A run whose column is identical down every row tells you nothing — delete
it.** A run that splits the rows in half is worth the most.

### 4. Pick the minimal discriminating set
Greedy is fine: take the run that splits the surviving explanations most
evenly per unit price; repeat until one explanation would remain. Usually two
to four runs. Always include:
- the **matched-budget baseline** (same params / compute / tuning effort);
- the **remove-only-the-claimed-mechanism** run.

### 5. Price and order
Per run: cost in the profile's currency (minutes, GPU-hours, €). Order by
information per price, cheapest decisive first. State the **stopping rule**:
which outcome ends the investigation early.

### 6. Pre-register
Write the predictions *before* running. File as
`<reports dir>/ablation-<slug>.md`; runs go in the ledger with prices. After
the runs, results are appended to the same file next to the predictions —
including the ones that embarrassed the favoured explanation — and the
conclusion goes through `lab:stage-report`.

## Template
```markdown
# Ablation plan: <effect>
**Date:** …  **Effect:** <number ± noise, n seeds>  **Noise known?** yes/no
## Rival explanations
## Prediction table
## Chosen runs (run · splits which · price · order)
## Stopping rule
## Results (filled in later, beside the predictions)
```

## Guards
- One variable per run. A run that changes two things is a new confound.
- Don't tune the ablated variant less than the full one.
- If the plan costs more than re-deriving the idea from scratch, say so.

End with the four-part TL;DR: the runs, the total price, what each outcome
would imply.
