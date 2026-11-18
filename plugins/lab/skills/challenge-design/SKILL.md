---
name: challenge-design
description: Run a structured first-principles challenge against an existing design choice — restate the constraint it serves in a real unit, re-derive the cheapest solution from scratch, and reach a verdict (survives / replaced / undecidable-without-measurement). Use before building on an existing component, when a choice is defended by convention or authority rather than by a constraint, when a number in a spec has no derivation, or when asked to challenge something. Generic version — if the project has its own skill named challenge-design, use that one instead.
argument-hint: [the choice to challenge]
metadata:
  group: decide
  phrase: "Challenge an existing choice from scratch: survives, replaced, or undecidable without a measurement."
---

# Challenge a design choice

**Choice under challenge:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults: decisions in docs/lab/decisions.md, ledger docs/lab/open.md; currencies = time, money, memory, bytes moved, energy, plus this project's own outcome metric. Say in one line that defaults are in use and that /lab:init would fix it."`

Working contract: [contract.md](../../reference/contract.md). Every existing
design choice is a **working hypothesis, not a settled decision**. This skill
is that challenge run as a procedure, so it produces an artifact instead of a
vibe.

## When to run it

- Before building on top of an existing component — the cheapest moment to
  find out the foundation is wrong.
- When a choice is defended by **convention or authority** ("it's the
  standard", "everyone uses X", "the parent project says so").
- When a number in a spec has no derivation behind it (a ceiling, a
  resolution, a timeout, a pool size).
- Whenever explicitly asked.

**Not** a reason to run it: code that works but isn't maximally elegant. This
produces decisions, not refactors. And if there is *no* incumbent at all, this
is the wrong skill — use `lab:derive-ansatz`.

## Procedure

### 1. Name the choice and find where it lives
Quote it and cite the file. If it isn't written down anywhere, that is the
first finding — an unrecorded choice can't be challenged, only guessed at.

### 2. Restate the constraint it actually serves, in a unit
This step does the work. Not "it's a good architecture" — what *quantity*, in
what *unit*, does this choice exist to satisfy? Use the profile's
**Currencies** table. (Typical ones: money per unit or per month;
milliseconds of a specific latency; KB/MB of peak working set or payload;
bytes moved per request/frame; joules; grams; engineer-hours; and the
project's headline outcome metric — the only one that ultimately counts.)

If you cannot name the unit, stop: the choice is serving a *habit*, not a
constraint, and the finding is that the constraint needs establishing first.
Say that — don't invent one to justify the answer.

### 3. Re-derive from scratch
Ignoring what exists, what is the **cheapest structure that satisfies that
constraint**? Design it as if nothing had been built. Do this *before*
re-reading the current implementation, so its framing doesn't anchor you.

The most common failure: **accepting the choice's own framing.** "Which
backbone?" presumes a backbone. "Which queue?" presumes asynchrony. "Which
cache?" presumes the read path is the problem. "Which chip?" presumes the
memory hierarchy is someone else's to choose. Challenge the question before
answering it.

### 4. Compare, honestly
Put the from-scratch answer next to the existing one, in the unit from step 2.
Include the cost of *changing*, which is real — migration, retraining,
invalidated results, anything downstream built on the current choice.

### 5. Verdict — one of exactly three
- **Survives.** Say why in one line and move on. A completely legitimate and
  common outcome; a challenge that can only ever conclude "replace it" is a
  rewrite with extra steps.
- **Replaced.** State the replacement concretely and record it with
  `lab:record-decision`, including what it supersedes.
- **Undecidable without measurement.** Name the specific measurement that
  would settle it, its price, and what each outcome would imply. Record it
  under `## Open / not yet decided` and in the open-questions ledger. Often
  the most honest verdict — not a failure to conclude.

Record surviving verdicts too: "we considered replacing this and didn't,
because X" is what stops the question being reopened every session.

## Guards

- **A challenge produces a decision, not automatically a diff.** "Replaced" is
  a proposal with a cost attached — not licence to start rewriting working
  code or invalidating existing results.
- **Don't re-litigate what's already been challenged.** Read the decisions
  file first. If an entry already contains the from-scratch reasoning, only
  new evidence reopens it.
- **Respect corrected-first-attempt entries.** If the log says an approach was
  tried and failed with numbers attached, proposing it again needs an
  explanation of why the recorded failure doesn't apply.
- **Cheap and fast beats correct and late.** A verdict of "build the rigorous
  version" must justify itself against iteration throughput, not just
  correctness.

End in the terminal with the four-part TL;DR (contract.md §5).
