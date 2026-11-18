---
name: derive-ansatz
description: Generate candidate solution forms for a NEW problem from first principles — state it as a constrained optimisation in real units, find its structure, solve the limiting cases, look for an isomorphism to something already solved, and write down 2–4 ansätze each with a priced kill test. Use when there is no incumbent design to challenge yet, when a problem is novel to the project, or when asked for intuition, a derivation, or "what should this even look like". Generic version — if the project has its own skill named derive-ansatz, use that one instead.
argument-hint: [the problem, as a question]
metadata:
  group: idea
  phrase: "New problem, nothing built: limiting cases, an analogy with its breaking points, 2-4 candidate solution forms, each with a kill test."
---

# Derive an ansatz

**Problem to derive:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults: derivations in docs/lab/derivations/, ledger docs/lab/open.md, hypotheses in docs/lab/hypotheses.md; currencies = time, money, memory, bytes moved, energy, plus this project's own outcome metric. Say in one line that defaults are in use and that /lab:init would fix it."`

The working contract these skills assume is in
[contract.md](../../reference/contract.md) — read it if you haven't this
session.

## What this is

An ansatz is a *guess at the form of the solution*, made deliberately so it
can be tested. Not a design, not a decision. The measurement is the point; the
derivation only decides which measurement is worth making. This skill exists
so the intuition produced when a problem is brand new becomes a filed,
falsifiable artifact instead of a good paragraph lost in chat.

Pipeline position: **derive → explore → challenge → record.**

**Not** for choosing between existing options (`lab:challenge-design`) or
summarising what others have done (`lab:explore-and-report`).

## Procedure

### 1. State the problem as a constrained optimisation, in real units
Three lines: **objective** (what is maximised, in what unit — the profile's
headline metric if it applies), **binding constraint** (one of the profile's
currencies), **free variables**. Include the things that look like givens but
are actually someone's to set — a rule, an interface, a budget, a deadline, a
tier. If you cannot name the unit of the objective or the constraint, stop and
say so: the problem isn't posed yet.

### 2. Find the structure before proposing anything
- **Symmetries / invariances** — translation, scale, reflection, permutation,
  time-shift, idempotence, commutativity. Each is either a constraint on the
  solution form or a free augmentation/test. Say which, and what enforcing it
  structurally would cost.
- **Timescales** — list them with rough magnitudes. Separated timescales
  almost always mean separable sub-problems.
- **Known vs. learned/searched** — which parts are exact and analytic (a
  physics model, a deterministic engine, a protocol spec, a type system)?
  Those should never be learned, guessed, or re-derived at runtime.
- **Where the cost actually is** — which part dominates the binding currency?
  It is rarely where intuition says.

### 3. Solve the limiting cases
Push each free variable and nuisance parameter to 0 and to ∞ (latency, noise,
memory, number of agents/users, horizon, budget, load). Each limit is usually
solvable on paper, and the general answer must interpolate between them. A
candidate that gets a limit wrong is dead — the cheapest kill available, so do
this before writing any ansatz down. If a crude interpolation formula falls
out, write it: a formula with a named exponent says what to sweep and what
curve to expect.

### 4. Look for an isomorphism
What already-solved problem has the same shape? Look **inside this project
first**, then outside. Write the mapping as an explicit table — this ↔ that —
with each row labelled **intuition** or **claim**, then a list: **where the
mapping breaks.** An analogy without a stated breaking point is decoration.

### 5. Write 2–4 ansätze
For each: the parameterised form (specific enough to implement in an
afternoon), what structure from step 2 it exploits, which limits from step 3
it gets right, and a one-line cost in the profile's currencies. Always include
**A0, the dumbest viable baseline** — the thing every other ansatz must beat.

### 6. Give each a kill test, with a price
The cheapest experiment that would falsify it, the result that kills it, and
what it costs (an afternoon, 10 € and a timer, a GPU-day). An ansatz with no
kill test is an opinion. Prefer one experiment that discriminates between
several ansätze over one each.

### 7. File it, with a status per ansatz
`<derivations dir>/<slug>.md` + a row in its `README.md` index (create both if
missing). Status per ansatz, exactly one of:
- **Promoted to hypothesis** — gets an H-number where the profile keeps live
  hypotheses, stated so it can be falsified, baseline named.
- **Parked** — plausible, kill test priced, not worth running yet. Say what
  would un-park it.
- **Killed** — by a limit, a symmetry, or a cost. Record *what* killed it;
  that is what stops it being re-proposed next month.

Append every priced kill test to the **open-questions ledger**
(item · price · raised-by · status). If the derivation reveals that a "given"
is really a free variable someone must set, that is a decision-in-waiting:
hand it to `lab:record-decision` for the `Open / not yet decided` section.

## Report template

```markdown
# <Problem, as a question>

**Derived:** <YYYY-MM-DD>   **Time spent:** <honest figure>
**Status:** <n promoted / n parked / n killed>

## Problem (objective · constraint · free variables)
## Structure (symmetries · timescales · known vs learned · where the cost is)
## Limiting cases  (table: limit → what wins → what it implies)
## Isomorphism  (mapping table with intuition/claim labels, then "where it breaks")
## Ansätze  (A0 baseline, A1…; form · exploits · cost)
## Kill tests  (table: test → discriminates → result that kills → price)
## Verdicts  (per ansatz: promoted / parked / killed, one line why)
## Hand-offs  (to explore-and-report, record-decision, the roadmap, the ledger)
```

## Guards

- **Derive first, search second.** Do steps 1–5 *before* reading the
  literature or the existing code on this problem — anti-anchoring. Then hand
  the ansätze to `lab:explore-and-report` to find which already exist.
  Rediscovering a known result is a good sign about the derivation, but it
  must be found and cited before anything is called novel.
- **Label every analogy: intuition or claim.** A claim is something a decision
  will rest on and needs a kill test.
- **Every number is measured, sourced, derived, or assumed — and says which.**
  Use the project's own constants where they exist rather than re-guessing
  them. When a derived number contradicts something said earlier in the
  session, that contradiction goes first in the TL;DR.
- **Time-cap it: one sitting.** If it wants a second day, the problem needs a
  measurement, not more derivation.
- **No implementation.** Code still starts in planning mode with
  `lab:challenge-design` — by then there is an ansatz to challenge.

End in the terminal with the four-part TL;DR (contract.md §5).
