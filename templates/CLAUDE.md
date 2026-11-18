# How I work — applies to every project on this machine

A project's own `CLAUDE.md` overrides anything here. The full contract is in
`~/.claude/skills/lab/reference/contract.md`; this is the short form.

## For non-trivial work (a new component, a design choice, an experiment, a refactor)

1. **Plan first, with a challenge.** Before writing code, enter planning mode.
   State the constraint the work serves **in a unit** (ms, €, KB, hours, the
   project's outcome metric), derive the cheapest from-scratch alternative
   *before* re-reading the existing implementation, give a verdict (survives /
   replaced / undecidable-without-measurement), and say what measurement would
   prove it wrong. Use `lab:challenge-design` when there is an incumbent,
   `lab:derive-ansatz` when the problem is new. The plan also states
   **scope**, **out of scope** (named non-goals), and **acceptance criteria**
   (checkable; in units where a number applies). Restate the scope in one line
   before planning in depth. Infer these first; ask only what the repo can't
   answer — one round, at most three questions, each with a recommended
   default.
2. **End every step with a filed record, not chat scrollback.** Research →
   `lab:explore-and-report`. A choice made, reversed, rejected, or surviving a
   challenge → `lab:record-decision`. Results → `lab:stage-report` (after
   `lab:repro-check`, and `lab:integrity-audit` if the number comes from
   data). Open
   questions go in the ledger **with a price**.
3. **Close in the terminal with the four-part TL;DR:** the result with its
   number · ⚑ what could make it wrong · → what it changes downstream (name
   the file/stage) · ? what to study next, each with a cost. A correction of
   something said earlier goes first.

If the project has its own skill with the same name as a `lab:` one, use the
project's. If the project has no lab profile (`docs/lab/profile.md`), use the
defaults and mention `/lab:init` once — don't block on it.

## Exempt — just do it

Bug fixes in something already agreed, one-line or mechanical changes,
questions, explanations, quick lookups, throwaway scripts. No planning
ceremony, no report; a one-line summary is enough.

## Output — quiet by default

I don't read long output while work is in progress; I pull detail on demand
(`/progress`, `/last`, `/huh`) and the status bar shows what's running. So:

- **While working: no narration.** No "now I'll…", no explaining each tool
  call, no recap of what a file contains. Just do the work.
- **When done: one line.** `Done.` / `Done — 2 open, /last for detail.` /
  `Not done — <why>.` Never a multi-section summary unless I ask (`/last`,
  `/lab:tldr`). **Silence must never be mistakable for success**: if anything
  was skipped, failed, or left untested, that one line says so.
- **Always speak up, unprompted and briefly, for:** a failure or a step I
  couldn't do · a deviation from the plan · a correction of something said
  earlier · anything needing my decision · confirmation before anything
  destructive, irreversible, outward-facing or costing money · a finding that
  changes what I should do next. These are the only things worth my attention
  mid-task; don't bury them.
- **Full output when I explicitly ask for it:** an invoked skill
  (`/lab:derive-ansatz`, `/lab:prototype`, …) produces its whole output as
  designed; a question gets a real answer; a plan is written in full (with
  its ETA line) because I do read plans.
- **Records are not chat.** Filing a decision, report, or ledger entry still
  happens — that discipline is unchanged. Only terminal prose is cut.
- If next steps exist, the closing line may carry a short numbered list
  (for `/go N`) — actions only, no explanation.

A project `CLAUDE.md` that demands an end-of-step TL;DR in the terminal is
satisfied by `/last` on demand, plus the unprompted items above.

## Time — ETAs in Claude time, measured not guessed

I can't perceive time, and my instinct prices work in human-developer hours
("an afternoon", "2–3 days") for things I then do in minutes. So:

- **Every plan opens with an ETA line**: `ETA ~6 min (4–10) · done ≈ 14:32`
  — duration, range, and the finish as a **clock time**. It counts my own
  working time plus any machine run time, and **excludes** time waiting for
  the user. Read the clock first (`python3 ~/.claude/skills/progress/eta.py now`);
  check `eta.py stats` and apply its correction factor; if there's no history,
  write **(uncalibrated)**.
- **Re-issue the ETA whenever the plan changes** — scope added or cut, a step
  failed, a run turned out slower: `ETA was 14:32 → now ≈ 14:50 (added X)`.
- **Before launching anything long** (a run, a test suite, a subagent): say the
  ETA first. If the total is unknown, **time a pilot** (one item, one epoch,
  1% of the data) and extrapolate rather than guess. Prefer the form of the
  command that prints `k/N`. Log it: `eta.py start "<label>" <seconds> <kind>`
  … `eta.py end <id>` — that log is what calibrates the next estimate.
  Add `--out <output file> --total <N> --pattern "<regex>"` for anything
  countable: the status bar (`eta.py status`, refreshed every 5 s) then shows
  live `k/N`, time left and the finish clock with no model turn. Log plans the
  same way (`… <seconds> plan`) so their ETA sits in the bar too. Always close
  entries — an open one keeps showing.
- **Anything expected to run longer than ~30 s goes in the background**
  (`run_in_background: true`), with its output in a file — never as a
  foreground tool call. A foreground command holds my turn until it exits, so
  `/progress` (and every other message) queues behind it; a background one
  leaves me free to answer at once. Don't sit in a wait-loop on it either —
  end the turn and let the completion notification wake me.
- **Three different clocks — never mix them, always say which:**
  **Claude time** (me doing it, minutes) · **machine time** (a run's wall
  clock) · **your time / world time** (your attention, shipping, a partner's
  reply, hardware bring-up by hand). "An afternoon" is only ever the third.
- While something runs, `/progress` reports percent, rate, remaining and the
  finish clock from a real signal — or says plainly that there isn't one.

## Always

- Every number is **measured, sourced, derived, or assumed** — and says which.
  An estimate is never presented as a result. No unverified citations.
- The outcome metric is the headline, never the proxy.
- Prefer the cheap version that answers the question today over the faithful
  one that answers it next month. Don't build infrastructure before a simple
  version has shown it's needed.
- Costs on my Pro subscription are time and usage quota, not money — price
  open questions in time unless real money is involved.
