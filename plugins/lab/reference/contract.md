# The lab working contract

The rules every `lab:` skill assumes. Project-specific values (which units,
which paths, which upstream) come from the project's **lab profile**
(`docs/lab/profile.md`); this file is the part that doesn't change between
projects.

## 1. Every existing design choice is temporary

Architectures, libraries, hardware picks, pipelines, numeric ceilings — all
working hypotheses. The purpose of a discussion is to challenge them against
first principles and improve them, not to elaborate on them.

- Restate the **constraint the choice actually serves**, in a physical or
  otherwise countable unit — not the choice itself.
- Ask what the **cheapest structure that satisfies that constraint** looks
  like, as if nothing had been built.
- If the existing choice survives, say why in one line and move on. If not,
  say so plainly, propose the replacement, and record it.

Decision logs record *why*, so a challenge can be informed rather than
ignorant. They are not a list of things that can't change.

## 2. The headline metric is the outcome, not the proxy

Every project has a proxy that is easy to measure (accuracy, loss, parameter
count, test coverage, lines changed) and an outcome that actually counts (lap
time, p99 latency under load, euros per month, user task completion). The
profile names the outcome. Never report the proxy as the headline.

## 3. Cost is a hard constraint, stated in real units

Prefer the solution that gets 80% of the result for 10% of the cost. When
proposing anything that costs money or time, quote the number and say what it
displaces.

## 4. Implementation starts in planning mode, with a challenge

No implementation work begins directly. Before writing code for a component,
enter planning mode and run `lab:challenge-design` (or `lab:derive-ansatz` if
there is no incumbent). The plan must contain:

- **The constraint**, in a unit.
- **The from-scratch alternative**, derived *before* re-reading the existing
  implementation so its framing doesn't anchor the answer.
- **The verdict** — survives / replaced / undecidable-without-measurement.
- **What would falsify it** — the measurement, and when it will be run.
- **Scope** — what this step delivers, as a list of things that will exist
  afterwards.
- **Out of scope** — named non-goals: the adjacent things that will *not* be
  done, especially the tempting ones. This is what stops a step growing.
- **Acceptance criteria** — how we will know it is done: checkable, and in
  units where a number applies ("`validate` passes", "p99 under 50 ms at
  1000 rps", "runs in an unrelated project with no skill text edited"). The
  falsifier tests the *design choice*; acceptance criteria test the
  *deliverable*. They are different and a plan needs both.

**Asking about scope.** Infer all three from the request, the repo and the
profile first. Ask only what those can't answer and what would change the
plan: **one round, at most three questions, each with a recommended default**
so the user can just say yes. Restating the scope back in one line before
planning in depth is cheap and catches a misread request early — do that even
when no question is needed. Never ask what can be looked up.

Applies to refactors too. Does not apply to fixing an outright bug in
something already agreed.

## 5. Every step ends in a record that carries measurements

Nothing is done while its result exists only in chat scrollback. Route by
kind — one monolithic report per step becomes ceremony:

| What happened | Skill | Where it goes |
|---|---|---|
| a new problem got a first-principles derivation | `lab:derive-ansatz` | derivations dir + index row |
| something external was researched | `lab:explore-and-report` | explorations dir + index row |
| a choice was made, changed, or rejected | `lab:record-decision` | the decisions file (and upstream, if the profile names one) |
| an implementation stage produced results | `lab:stage-report` | reports dir |
| a question was left open | any skill | the open-questions ledger, **with a price** |

A report whose content is "these files were written" is not a report. If a
step produced no measurement and falsified nothing, say that in one line and
move on.

### The TL;DR contract — how every step ends in the terminal

The written record is for later; the terminal is where decisions get made.

```
TL;DR      one or two sentences: what happened, and the number.
⚑ Flagged   what could make this wrong.
→ Implies   what this changes downstream — name the stage, hypothesis, file.
? Deeper    what to study next, each with a cost.
```

- **Lead with the number, not the narrative.** "516.5 KB against 512 KB —
  infeasible by 4.5 KB" beats "the model turned out not to fit."
- **⚑ Flagged is mandatory and specific**: every assumed input, every constant
  that is a guess, every result not measured on the real thing. If nothing is
  flagged, say *why* the result is safe — never leave it empty.
- **A contradiction of something said earlier goes FIRST**, above the TL;DR.
  Corrections are the highest-value line in any summary.
- **→ Implies must name a target.** "We should consider…" is not an
  implication.
- **? Deeper items carry a cost, and say in which clock**: **Claude time**
  (me doing it — minutes, e.g. "~20 min Claude"), **machine time** (a run's
  wall clock — "~3 h on the laptop", ideally from a timed pilot), **your time
  / world time** (your attention, a purchase, shipping, a reply, bring-up by
  hand — "10 € + an afternoon of yours"). Never quote human-developer days for
  work Claude will do. Uncalibrated estimates say so.
   An open
  question without a price is a wish, and wishes accumulate. Append them to
  the ledger so they don't evaporate either.
- **Don't restate the report.** Scannable: tables over prose, bold the numbers
  that matter, and stop.

## 6. Optimise for iteration throughput, not per-experiment polish

A toy that answers the question in 30 seconds beats a faithful version that
answers it next month. Prototype, measure, then decide whether the expensive
version is warranted.

- Cheap proxies and simulators are first-class tools.
- Measure on the real target before claiming a result about it; an estimate
  is not a result.
- Don't build search/tuning/framework infrastructure before a simple version
  has shown it's needed.

## Provenance — the rule that makes the numbers trustworthy

Every number is one of: **measured** (say what ran, where the data is),
**sourced** (cite it, URL verified), **derived** (from the steps shown), or
**assumed** (an engineering guess — *say so in that word*). An assumed number
and a sourced number must never look alike. No fabricated or unverified
citations, ever.
