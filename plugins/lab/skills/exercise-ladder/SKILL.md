---
name: exercise-ladder
description: Write a graded set of exercises on one concept — the same idea at several difficulty rungs, each with a checkable answer (a test, an expected output, a number), a hint ladder, a worked solution, and the misconception it is designed to expose.
disable-model-invocation: true
argument-hint: "<concept>" [--rungs 3] [--lang python] [--minutes-per-rung 10] [--autocheck] [--out <dir>]
metadata:
  group: organise
  phrase: "One concept at several difficulty rungs, each with a checkable answer, hints, and the misconception it exposes."
---

# Exercise ladder

**Arguments:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Fine for this skill — infer context from the arguments."`

## Flags
| Flag | Meaning | Default |
|---|---|---|
| `--rungs` | number of difficulty levels | 3 |
| `--lang` | language / tool for the exercises | python |
| `--minutes-per-rung` | target solve time for the intended audience | 10 |
| `--autocheck` | ship runnable tests / a checker script per rung | off (expected outputs only) |
| `--out` | where to write | `exercises/<slug>/` |

## Design rules

1. **One concept, isolated.** State it in a sentence. Each rung varies the
   *difficulty of applying it*, not the topic. Incidental difficulty (parsing
   input, fiddly setup, obscure API) is removed — give starter code for
   everything that isn't the concept.
2. **The rungs**
   - **Rung 1 — recognise / apply directly.** One step, the concept in its
     plainest form. Nearly everyone succeeds; it builds the vocabulary.
   - **Rung 2 — apply where it isn't labelled.** The learner must notice the
     concept is relevant. Includes the **classic trap**.
   - **Rung 3 — combine, or find the limit.** Compose with one other known
     idea, or find where the naive approach breaks (scale, edge case, noise,
     a constraint in real units).
   - Further rungs: open-ended, with a measurable target ("under 50 ms",
     "under 512 KB") instead of a single right answer.
3. **Every rung has a checkable answer.** A test, an exact expected output, a
   number with a tolerance, or a property that must hold. "Discuss" is not
   checkable. With `--autocheck`: a test file or checker per rung that prints
   a useful message, not just pass/fail.
4. **Name the misconception each rung is built to expose** — and make the
   wrong answer that misconception produces *checkably* wrong, with a message
   that points at the idea rather than the fix.
5. **Hint ladder, three steps:** a nudge (where to look) → the key idea → the
   first line of the solution. Hints are separate so they can be revealed one
   at a time.
6. **Worked solution** that explains *why*, plus one common alternative and
   why it's worse or equivalent.

## Procedure

1. State the concept, the prerequisite knowledge, and the audience.
2. List 2–4 real misconceptions about it (from experience, or from how the
   concept is commonly mis-taught). These drive the rungs.
3. Draft the rungs; for each: prompt · starter · check · misconception ·
   hints · solution · target minutes.
4. **Solve every rung yourself from the starter code and run every check.**
   Also run the *misconception's* answer through the check and confirm it
   fails with the intended message. Report what was run.
5. Calibrate: if your own solve time × 3–4 exceeds `--minutes-per-rung`,
   cut or split the rung.
6. Write to `--out`: `README.md` (concept, prerequisites, how to check),
   `rung-N/` (prompt, starter, check), `hints/`, `solutions/`.

## Guards
- No trick questions — difficulty comes from the concept, never from ambiguity.
- A rung that can be passed by pattern-matching the previous rung's solution
  isn't a new rung.
- Untested checks are labelled untested.

End with: the concept, the misconception per rung, and what was actually run.
