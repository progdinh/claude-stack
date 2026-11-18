---
name: go
description: The shortest way to say "proceed". With a number (or several) — do that item from the numbered list of next steps Claude last proposed. With nothing — resume whatever was interrupted or pending, exactly where it stopped, no questions asked ("go again, sorry, misclick"). Use for "/go", "/go 2", "/go 1 3", "/go all", "go", "continue", "carry on", "yes do it", "resume", or right after an accidental interrupt.
argument-hint: [N | N M … | all | next]   (nothing = resume what was interrupted)
effort: low
metadata:
  group: reflex
  phrase: "Proceed. /go 2 does item 2 of the last numbered list; bare /go resumes whatever was interrupted, no questions."
---

# go — proceed

**Argument:** $ARGUMENTS

The user is saying yes with as few keystrokes as possible. Don't make them
repeat themselves, don't ask them to confirm what they just confirmed, and
don't recap before acting. **Act first; one line saying what you're doing.**

## Resolve the argument

| Typed | Means |
|---|---|
| *(nothing)* | **Resume.** Whatever was interrupted, paused, or left pending — pick it up exactly where it stopped. |
| `N` | Item **N** of the most recent numbered list of next steps / options I proposed. |
| `N M …` | Those items, in the order given. |
| `all` | Every item of that list, in the list's order. |
| `next` | The first item of that list not yet done. |
| anything else | Treat it as a plain instruction to proceed with that thing. |

### Bare `/go` — resume
Look back for the most recent unfinished thing, in this order:
1. **An interrupted turn** — a tool call or a multi-step task cut off mid-way
   (an "Interrupted" marker, an abandoned edit, a half-run plan). Assume the
   interrupt was accidental. Resume from the step that was cut, not from the
   beginning; don't redo steps that completed — check what landed (a file
   exists, a command's output is there) if unsure, with one quick look.
2. **A question I asked that's still open** where I gave a recommendation →
   take my recommended option.
3. **A numbered next-steps list** with nothing chosen → item 1.
4. **A plan awaiting approval** → if it's in plan mode, present it for approval
   the normal way; `/go` isn't a substitute for the plan-approval step.

Say which one you picked in one short line ("Resuming the generator run —
metadata step already landed."), then do it. No apology theatre for the
interruption, no "would you like me to…".

### `/go N` — pick from my last list
Use the **most recent** numbered list I wrote that offered things to do
(next steps, options, a `? Deeper` block, a triage's proposed edits). Quote the
item's first few words so it's clear which one ("→ 2: the update-docs skill
file"), then do it. If there are two candidate lists, use the later one. If
**N doesn't exist**, or there is genuinely no list, say so in one line and show
the list you think was meant — don't guess a different action.

## The one thing `/go` does not override
A numbered item that is **destructive, irreversible, outward-facing, or costs
real money** (deleting data, force-pushing, sending/publishing something,
buying, spending paid credits) still gets its normal one-line confirmation —
`/go 3` selects it, it doesn't pre-authorise it. Everything else: just go.

## The other half: how I should write lists, so `/go` works

Whenever I propose what to do next — at the end of a step, in `? Deeper`, when
offering options, when reporting what's left after an interrupt:

- **Number them, one action per line, 1-based, imperative, short.**
  ```
  1. Write the unified generator script          ~4 min Claude
  2. Write the update-docs skill file            ~2 min Claude
  3. Regenerate and render-check both PDFs       ~3 min Claude + ~20 s machine
  ```
- Put the **recommended one first**. Give each its price and its clock
  (Claude / machine / your time).
- Only **one** numbered list of actions per message, at the end, so `/go N` is
  never ambiguous. Use bullets, not numbers, for anything that isn't a choice.
- Items are independent where possible; if 3 needs 1, say "3 (after 1)".
- After an interrupt, don't ask an open "what should I do?" — say what was cut
  and offer: `1. Resume from <step>  2. Stop here  3. Undo what landed`.
