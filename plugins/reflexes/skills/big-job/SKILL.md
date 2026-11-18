---
name: big-job
description: Bring back the multi-step job that was under way before the conversation diverted — show its checklist of phases with each one's CURRENT state (done / partly / not started / dropped), verified against what actually landed, then offer the remaining phases as a numbered list to resume. Use for "/big-job", "back to work", "where were we on that", "what's left", "what was the to-do list", "what were we doing before this", after a run of side questions or an interrupt.
argument-hint: [previous | N jobs back | the job's name]
effort: low
metadata:
  group: reflex
  phrase: "Back to the multi-step job we left: its phase checklist with current states, and the remaining phases numbered to resume."
---

# big-job — the job we left, and what's left of it

**Hint from the user:** $ARGUMENTS

## Find the job
A **big job** is a piece of work with several phases: a plan, a build with
steps, a to-do list I wrote, a phase/state table, a roadmap stage. Side
questions, `/huh`s, one-off skill requests, and meta-talk are not jobs.

- Default: the **most recent big job that isn't finished**. If the most recent
  one is finished, say so in one line and show the one before it.
- `previous` / `N` → further back. A name → that job.
- Use **its own phase list, as I wrote it** — same wording, same order — so the
  user recognises it. Don't re-plan it or merge phases. If phases were added
  mid-way (a request that arrived during the job), append them, marked `(added)`.

## Update every state — from evidence, not memory
For each phase, check what actually landed (the file exists, the command's
output is there, the test ran): one quick look per doubtful phase. States:

| State | Means |
|---|---|
| **Done** | landed, and checked/ran if that applies — say which |
| **Done, untested** | written but never run |
| **Partly** | what exists, what doesn't |
| **Not started** | |
| **Dropped** | and why — superseded, no longer needed |

## Output — this shape, nothing else

**<the job, in one line>** · started <clock time if known> · <k of n phases done>

| Phase | State |
|---|---|
| … | … |

**Interrupted by** *(one line)*: what we went off to do instead.

**Resume**
1. <the next unfinished phase, as worded above>          <price, which clock>
2. <the one after>
3. …
(last) Stop here — leave the rest

## Rules
- The table is the point. No prose recap of the job or the digression.
- A phase I *said* was done but can't confirm is **Done, untested** or
  **Partly** — never upgrade a state from memory.
- If the job had an ETA entry (`eta.py`), give elapsed vs estimate in the
  header, and re-issue the ETA for what's left.
- Don't start working — wait for `/go N` or a yes.
- If a decision of the user's is blocking the next phase, item 1 is that decision.
- No unfinished big job anywhere → say so in one line.
