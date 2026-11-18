---
name: progress
description: Report how far along a running background job is — a shell command, a training run, a test suite, a subagent — and when it will finish, as a clock time. Measures instead of guessing: finds a real progress signal (a k/N counter, files produced, log lines, epochs), computes the recent rate, and gives percent done, elapsed, remaining, and the finish time; flags stalls; says plainly when no estimate is possible. Use for "/progress", "how long left", "is it still running", "when will that finish", "ETA?", "is it stuck".
argument-hint: [process id | task id | label]   (none = everything running)
effort: low
metadata:
  group: reflex
  phrase: "How far along is a running job, and when does it finish? Percent, rate, remaining and a clock time, from a real signal."
---

# progress — how far, how long, finishing when

**Target:** $ARGUMENTS

Helper (clock, rate maths, calibration log): `${CLAUDE_SKILL_DIR}/eta.py`
— run `python3 ${CLAUDE_SKILL_DIR}/eta.py --help` for its commands.

**I cannot perceive time.** Every duration here comes from a clock read
(`eta.py now`, `ps -o etime`, file mtimes, timestamps in the log) — never from
a feeling about how long it's been.

## The status bar already answers most of this

`~/.claude/settings.json` has a `statusLine` running `eta.py status` every 5 s:
any logged plan or watched job is visible at the bottom of the terminal
permanently, instantly, without invoking this skill or waiting for a turn.
This skill is for the detail the bar can't give (drifting rates, stalls, jobs
nobody registered, subagents) — and a skill is a prompt, so it **queues behind
a running turn**; the bar doesn't.

## 1. Find the job(s)
No argument → every background task this session started, plus anything
obviously long-running it launched. With an id/label → that one. For each:
what it is, when it started (clock), and **elapsed** — from the task's start
record, `ps -o etime= -p <pid>`, or the first timestamp in its output.

Read its output so far with whatever this session provides for background
tasks (task output / its log file / the file it writes). Read the **tail**,
not everything.

## 2. Find a progress signal — best available, in this order

| # | Signal | How |
|---|---|---|
| 1 | **Explicit counter** in the output: `14/25`, `epoch 3/10`, `62%`, a tqdm bar, `[ 340/1200]` | done, total straight from the last line |
| 2 | **Artefacts on disk**: output files, checkpoints, rows written vs the number expected | count them (`ls \| wc -l`), total from the command's inputs |
| 3 | **Known work list**: the command loops over N inputs and logs each one | count log lines matching the per-item pattern |
| 4 | **Phases**: build → test → package; k of n phases done | coarse — say it's coarse |
| 5 | **History only**: this same command has run before (`eta.py stats <label>`) | elapsed vs the typical total |
| — | **None** | go to step 5 |

State which signal was used. Never invent a total.

## 3. Compute — with the recent rate, not the lifetime average
`python3 ${CLAUDE_SKILL_DIR}/eta.py rate <done> <total> <elapsed_s>` gives
percent, per-item rate, remaining and the finish clock. But first check
whether the rate is steady: compare the **last ~5 items'** pace (from output
timestamps or file mtimes) with the overall pace.
- Steady → use overall.
- Slowing or speeding up (warm-up, growing inputs, cache effects, thermal
  throttling) → use the recent rate, and say which way it's drifting.
- Items differ wildly in size → say the estimate is loose, give a range.

Add known fixed tails (a final evaluation, a save, an upload) if the command
has them.

## 4. Report — one block per job, this shape

```
<label>                                          started 14:02
████████████░░░░░░░░ 62% · 14/25 circuits        signal: counter in output
elapsed 8m12s · 35s/item (last 5: 41s, slowing)
remaining ~7m (6–9) · done ≈ 14:17
```

- **Remaining as a duration AND the finish as a clock time.** Clock times are
  what the user plans around.
- Always a range when the rate isn't steady.
- These are **machine wall-clock** figures: how long *this process on this
  machine* will take. Never a human-effort estimate.
- Stall check: if the time since the last output line (or last file written)
  exceeds ~3× the typical gap between items → `⚠ possibly stalled: no output
  for 4m10s, typical gap 35s` and the one most likely cause to check (waiting
  on input, a lock, OOM, network).
- Finished already? Say so, with its actual duration and exit status — and
  close its log entry (`eta.py end <id>`).

## 5. When there is no signal — say so, don't guess

```
<label>   started 14:02 · elapsed 8m12s · still running (CPU 97%, last output 12s ago)
No progress signal: the command prints nothing countable and the total is unknown.
To make it estimable next time: <the specific change — print k/N per item,
  use --progress, write one file per item, log epochs>.
```

Alive-or-dead is still answerable: CPU use, last-output age, output growing.
If `eta.py stats <label>` has history for this command, give elapsed vs its
typical total, labelled as history-based.

## Subagents

A subagent has no counter. Report: started, elapsed, last activity, what it
last did (if visible), and — if `eta.py stats agent` has history — elapsed vs
the typical run. Say **low confidence** unless the agent was given a
countable work list (then treat it as signal #3). Never fabricate what a
running agent has found; report only what its output shows.

## Before launching something long (the other half of this skill)

1. **Make it measurable**: prefer the form of the command that prints `k/N`
   or a progress bar; add one if it's our own script.
2. **Pilot, then extrapolate**: if the total is unknown, time 1–2 items (or
   one epoch, or 1% of the data) and multiply. A 20-second pilot beats any
   guess. Say `ETA ~12m (pilot: 29s/item × 25), done ≈ 14:31`.
3. **Log it, and make it watchable**:
   `eta.py start "<label>" <est_seconds> shell --out <the task's output file> --total <N> --pattern "<regex matching one line per finished item>"`
   → the **status bar** then shows a live `▓▓▓▓░░ 14/25 · ~6m left · ≈14:17`
   every 5 s with no model turn — the user never has to ask. Without
   `--out/--total/--pattern` it shows elapsed vs estimate instead.
   `eta.py end <id>` when it finishes; that history is what makes the next
   estimate honest. Do the same for plans: `eta.py start "<plan label>" <s> plan`.

## Rules
- Clock reads, not vibes. If I didn't read a clock, I don't state a duration.
- Don't interrupt, restart, or "help" the running job. Read-only.
- Don't poll in a loop. One report; the harness notifies when the job ends.
- No signal + no history = "can't estimate", stated plainly. That's an
  acceptable answer; a made-up number isn't.
