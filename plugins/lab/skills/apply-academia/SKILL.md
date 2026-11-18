---
name: apply-academia
description: Take a PROVEN idea from the literature (a paper, method, architecture, algorithm) and work out how — and whether — to implement it in this project under its real constraints. Pins down exactly what was proven and at what scale, measures the gap to this project's budget in orders of magnitude, splits the idea into separable mechanisms, and gives each a verdict (adopt / adapt / training-or-offline-only / reject) with a scaled-down reproduction and priced kill tests. Use for "apply X to our problem", "can we use <paper> here", "port <method> to <target>", e.g. "JEPA on edge AI". Differs from derive-ansatz (no prior idea) and explore-and-report (describes, doesn't port).
argument-hint: <idea or paper> on <target/application>
metadata:
  group: idea
  phrase: "Port a proven paper or method under your constraints: gap in orders of magnitude, verdict per mechanism (adopt / adapt / offline-only / reject)."
---

# Apply an academic idea to this project

**Idea → application:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/ and generic currencies (time, money, memory, bytes moved, energy, the project's outcome metric). Say so in one line; suggest /lab:init."`

Working contract: [contract.md](../../reference/contract.md).

The failure this skill prevents: an idea that works at the paper's scale gets
adopted whole, and three weeks later it turns out the part that made it work
was the part that doesn't fit. Papers prove a *result under conditions*; a
project needs a *mechanism under constraints*.

## Procedure

### 1. Pin the claim
From the primary source (verified URL — run `lab:explore-and-report` first if
no report exists; link it rather than restating it):
- **What exactly was shown**, as one sentence with its number and metric.
- **Under what conditions**: model/data/compute scale, hardware, latency
  regime, training budget, how many seeds, which baselines.
- **What it was NOT shown on** — especially anything resembling this project.

### 2. Measure the gap, in the project's currencies
One table: for each binding currency in the profile — the paper's operating
point, this project's budget, and the **ratio**. Orders of magnitude, with
provenance (sourced from the paper / derived / assumed). A 3× gap is an
engineering problem; a 10³× gap means the idea as published is not what gets
applied — go to step 3 before concluding anything.

### 3. Decompose into separable mechanisms
Almost every paper bundles several ideas: an objective, an architecture, an
inference-time procedure, a data recipe, a training trick. List them. For
each: is it needed at **training/offline time only** or at
**inference/run time**? What does it cost in each currency on its own? Which
one carries the result, according to the paper's own ablations (cite the
table) — and which are along for the ride?

### 4. Find the load-bearing assumption
What does the method silently rely on that this project doesn't have — scale,
a pretrained backbone, abundant labels, a GPU at inference, i.i.d. data,
a stationary environment, floating point? State it, and say whether the effect
is known to survive without it. "Does the effect exist at our scale at all?"
is the first question, and usually nobody has published the answer.

### 5. Name the cheap incumbent it must beat
The dumbest thing in this project that already addresses the same need (often
a loss tweak, a label shift, a lookup table, a heuristic). The academic idea
earns its complexity only by beating that, **on the outcome metric**.

### 6. Verdict per mechanism — exactly one each
- **Adopt** — fits as published.
- **Adapt** — state the modified form specifically enough to implement in an
  afternoon, and what is lost relative to the paper.
- **Training-time / offline only** — zero run-time cost; discarded at export.
  Say how "discarded" gets *verified*, not assumed.
- **Reject** — with the ratio or the assumption that killed it, so it isn't
  re-proposed next month.

### 7. The scaled-down reproduction, and kill tests with prices
Before any port: the smallest experiment that shows the effect exists at this
project's scale (toy data, tiny model, a simulator). Then per surviving
mechanism, a kill test: the result that kills it and what it costs. Prefer one
experiment that discriminates several mechanisms.

### 8. File and hand off
`<derivations dir>/apply-<slug>.md` + index row (prefix the Problem column
with "Apply:"). Priced tests → ledger. Verdicts that change or reject a design
choice → `lab:record-decision`. **No code yet**: implementation starts in
planning mode with these verdicts as its input.

## Template

```markdown
# Apply: <idea> → <application>
**Date:** …  **Source:** [title](verified URL) · report: <link>  **Status:** n adopt / n adapt / n offline-only / n reject
## The claim, pinned (result · conditions · not shown on)
## Gap table (currency · paper · our budget · ratio · provenance)
## Mechanisms (what · train-time or run-time · cost alone · does it carry the result?)
## Load-bearing assumption
## Incumbent to beat
## Verdicts
## Scaled-down reproduction + kill tests (test · kills what · price)
## Hand-offs
```

## Guards

- **The paper's headline metric is usually this project's proxy.** Judge by
  the profile's outcome metric.
- **Never quote a number from memory of a paper** — fetch it, cite the table.
- **A rejection is a result.** "No formulation of X fits budget Y, and here is
  the wall it hits" is worth filing precisely.
- **Check the decisions log first** — if this idea was already rejected with
  numbers, only new evidence reopens it.

End with the four-part TL;DR.
