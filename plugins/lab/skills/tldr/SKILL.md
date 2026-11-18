---
name: tldr
description: Summarise in the terminal where the project or a stage currently stands — what changed and the number, what is flagged as uncertain, what it implies downstream, and what deserves deeper study with a price on each item. Use when asked for a recap, a status, "where are we", "what did we learn", or to re-orient after a long session or a context boundary. Generic version — if the project has its own skill named tldr, use that one instead.
argument-hint: [optional: a stage or topic to scope the recap to]
metadata:
  group: start
  phrase: "Where is the project? State of play read from its files, blocking item first, every open item priced."
---

# TL;DR — terminal recap

**Scope:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Look for state in: docs/lab/ (decisions.md, open.md, derivations/, explorations/, reports/), any docs/roadmap.md or docs/decisions.md, CLAUDE.md, README.md, and recent git log. Say in one line that defaults are in use and that /lab:init would fix it."`

## Which recap is being asked for?

- **"The step that just finished" / "what did we just do" / "this session"**
  → the source is **this conversation**. Use it, in the four-part contract
  below. Do *not* go to git history or old docs to find "a step" — if there is
  no conversation to summarise, say so in one line rather than recapping the
  last commit. (For a plain six-line digest of the last turn, `/last` is the
  lighter tool.)
- **"Where are we" / a stage name / coming back after a break** → project
  state, read from the files listed further down.

## The contract

```
TL;DR      one or two sentences: what happened, and the number.
⚑ Flagged   what could make this wrong.
→ Implies   what this changes downstream — name the stage, hypothesis, file.
? Deeper    what to study next, each with a cost.
```

- **Lead with the number, not the narrative.**
- **⚑ Flagged is mandatory and specific** — every assumed input, every guessed
  constant, every result not measured on the real thing. If nothing is
  flagged, say *why* the result is safe; never leave it empty.
- **A contradiction of something said earlier goes FIRST**, above the TL;DR.
- **→ Implies must name a target.** "We should consider…" is not an
  implication.
- **? Deeper items carry a cost.** An open question without a price is a wish.
- **Don't restate the reports.** Tables over prose, bold the numbers that
  matter, and stop.

## What differs when recapping accumulated state (vs closing one step)

Someone has lost the thread. They need the state of play, not a narrative of
what was done.

1. **Lead with the current blocking item**, not history: the next decision or
   measurement that unblocks the most.
2. **Open hypotheses get a status each** — proposed / gated / testing /
   confirmed / killed — and what would move them.
3. **Roll up ⚑ Flagged across stages.** An assumption made once and consumed
   by three later stages is a bigger risk than the same assumption used once.
   Say where it propagated.
4. **Say what has NOT been measured on the real target** (real hardware, real
   traffic, real users, real data). The easiest caveat to lose after a run of
   green checkmarks in simulation or staging.
5. **List corrections made since the last recap**, so nobody acts on a
   superseded number.
6. **Read the open-questions ledger**: the cheapest unanswered items that
   unblock the most go in `? Deeper`; note stale ones.

## Where to read state from, in this order

Per the profile's Paths table: roadmap (stage status) → decisions file,
especially `## Open / not yet decided` (usually the real answer to "what's
blocking") → live hypotheses → the ledger → explorations and derivations
indexes (incl. "Still to file") → the most recent stage reports' residuals.

Prefer these over your memory of the session: the files are what survived, and
a recap that quotes chat scrollback will drift from the record. If something
important from this session is *not* in the files yet, say so and name the
skill that would file it.

## Hard rules

- **Never invent a status.** If it's unclear from the files, say unclear —
  don't infer completion from the existence of code.
- **Corrections first** — acting on a stale number is the most expensive
  failure a recap can cause.
- Readable in a terminal without scrolling twice. If it can't fit, the top
  item is wrong — pick the one thing that unblocks the most and lead with it.
