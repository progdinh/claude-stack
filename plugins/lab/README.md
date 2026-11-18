# lab — a first-principles research process, as a Claude Code plugin

**Using it? Read [GUIDE.md](GUIDE.md).** This file is for maintaining it.

Install from the marketplace (`/plugin install lab@sevel-stack`). Skills are
namespaced (`/lab:…`), so they never shadow a project's own skills.

| Skill | Use it when | Leaves behind |
|---|---|---|
| `/lab:init` | once per project | `docs/lab/profile.md` (the lab profile) + record folders |
| `/lab:run <question>` | work a problem end to end | the whole chain below, one TL;DR |
| `/lab:derive-ansatz` | the problem is new — no incumbent | a derivation: limits, isomorphism, 2–4 ansätze with priced kill tests |
| `/lab:explore-and-report` | something external gets researched | a sourced report + index row |
| `/lab:challenge-design` | about to build on, or defend, an existing choice | a verdict: survives / replaced / undecidable-without-measurement |
| `/lab:record-decision` | a choice is made, reversed, rejected, or survives | a decisions-log entry, incl. the wrong first attempt |
| `/lab:stage-report` | a stage or experiment produced results | a report carrying numbers, what was falsified, what broke |
| `/lab:tldr` | "where are we" | a four-part terminal recap |

**Research**

| Skill | Use it when | Leaves behind |
|---|---|---|
| `/lab:prototype <idea> [--stage poc\|prototype\|mvp] [--budget] [--deadline] [--team] [--build]` | an idea is being proposed: "what would this take?" | one-page brief: riskiest assumption → stage, smallest test, build/fake/skip, needs, effort range, done/kill criteria |
| `/lab:draft-ideas <theme> [--n 12] [--wild]` | the problem is still too vague to derive on | ranked idea list in `ideas.md`, kills included |
| `/lab:apply-academia <idea> on <target>` | porting a proven paper/method under this project's constraints | gap table, per-mechanism verdicts (adopt / adapt / offline-only / reject), scaled-down repro + kill tests |
| `/lab:novelty-claim <idea> [--depth scan\|standard\|thorough]` | before the word "novel" goes anywhere | logged queries, nearest-neighbour table, defensible claim wording |
| `/lab:ablation-plan <effect>` | a result's cause is assumed, not shown | pre-registered minimal discriminating runs, priced |
| `/lab:repro-check <result>` | a number is about to be cited or built on | reproducible / partially / not, with the missing piece |
| `/lab:integrity-audit <pipeline>` | any result that comes from data; anything too good | leak checklist with file:line, tripwire results |
| `/lab:perf-investigation <problem>` | slow / too big / too expensive | budget breakdown, before→after, what didn't help |
| `/lab:rule-stress-test <rule> [--adversary student\|pro\|lawyer]` | a rule, rubric, or reward someone will optimise against | exploit · fairness · enforceability tables, minimal patches |

`explore-and-report` takes `--depth scan|read|deep` (this is where a separate
"paper-read" skill was folded in rather than added).

**Manual-only** (`disable-model-invocation` — zero context cost until typed)

| Skill | Flags |
|---|---|

Pipeline: **(draft) → derive → explore → challenge → record → (plan → build →
repro-check → stage-report) → tldr.**

## How it adapts to a project

Every skill injects the project's **lab profile** (`docs/lab/profile.md`, or
`.claude/lab.md` if one exists there): headline
metric, the currencies that bind there, where records live, upstream repos,
house rules. No profile → documented defaults under `docs/lab/`, stated in one
line. The invariant part of the process is `reference/contract.md`.

## Verified (2026-09-19, Claude Code 2.1.277)

| Check | Result |
|---|---|
| `claude plugin validate` | passed |
| `claude plugin list` | loaded, user scope |
| `/lab:init` in an unrelated project (URL shortener, no hardware) | profile with web currencies (p99 @ 1000 rps, EUR/month, vCPU, pool depth), provenance tags, "not established" section — no skill text edited |
| `/lab:derive-ansatz` there | derivation filed + indexed, ledger updated, 4 ansätze (1 killed / 2 promoted / 1 parked); 12 turns, 0.32 USD on Sonnet |
| `/lab:tldr` with a profile | correct recap (8 turns) |
| no-profile fallback | injection line tested in a shell only (prints the defaults message, exit 0) — **not yet run end-to-end through a skill** |
| Name collision with a project-local skill of the same name | Claude picks the project-local `derive-ansatz`, treats `lab:` as fallback |

| `/lab:draft-ideas … --n 8` (v0.2.0) | 8 turns; checked the existing derivation, folded a duplicate into it, kept the kill on record, priced the top three; wrote `ideas.md` |

| Personal reflex skills exercised live by the user | `/huh`, `/last`, `/go`, `/rectify` (x3), `/your-take`, `/progress`. Not yet run: `/where`, `/big-job`, `/update-context` beyond its flag path |

| `/lab:stale` scanner on a multi-track research repo (v0.4.0) | first run raised 83 dead refs + 7 imports; after tightening (basename lookup, path-token filter, `ast` imports, sibling-track packages) **44 + 2**; hand-verified: 5 real findings, the rest examples / external repo names / dataset keys / historical citations. The judgement pass, not the scanner, found the most important one (a status row that lies) |

v0.2.0 skills **not yet exercised on a real task**: `apply-academia`,
`novelty-claim`, `ablation-plan`, `repro-check`, `integrity-audit`,
`perf-investigation`, `rule-stress-test`. All
validate and share the tested injection line. Expect each to need one round of
edits after its first real use — `derive-ansatz` was written against a real
problem the same day and is the better for it.

Not yet exercised: `/lab:run`, `/lab:stage-report`, `/lab:challenge-design`,
`/lab:record-decision`, `/lab:explore-and-report` (ported text, injection line
shared with the tested skills), and multi-track repos.

## Editing

`SKILL.md` edits take effect live. Changes to `plugin.json` or `reference/`
need `/reload-plugins`. Check with `claude plugin validate plugins/lab`.

## Sharing

This plugin ships through the `sevel-stack` marketplace in this repository.

## Decisions

### Skills-directory plugin, not plain personal skills
**Decision:** package as a plugin with a
`.claude-plugin/plugin.json` manifest.
**Why:** the constraint is minutes of attention to get the process into a new
project (was ~30 min of copy-and-rewrite per project, with drift; target one
command). Plain personal skills were the obvious cheaper option but Claude
Code's name precedence is Enterprise > **Personal > Project**, so a personal
`derive-ansatz` would shadow a specialised project-local one. Plugin skills are namespaced, so both coexist. A
marketplace plugin was deferred: it is copied into a cache and updated by
version bump, wrong for something edited daily.
**Would be reopened by:** the profile abstraction failing in a second project
(skill text needing hand edits to make sense there), or Claude preferring the
generic skill over a project's specialised one.

### Per-project profile instead of per-project skill copies
**Decision:** everything project-specific (units, paths, upstream, house
rules) lives in `docs/lab/profile.md`, injected into each skill with a shell
one-liner that falls back to defaults rather than failing.
**Why:** the original skills hard-coded one repo's tracks, units and
regulation numbers; copies would drift. One profile file per project is the
smallest thing that removes every hard-coded reference.
**First attempt, corrected after the first headless test (2026-09-19):** the
profile was specified at `.claude/lab.md`. `claude -p "/lab:init"` with
`--permission-mode acceptEdits` wrote every `docs/lab/` file but was **blocked
from writing under `.claude/`** (permission-gated directory) and staged the
profile elsewhere with a manual `mv` instruction. Root cause: choosing the
location by where config "belongs" rather than by what can be written in every
permission mode. Fix: default to `docs/lab/profile.md`; skills read both.
**Second corrected attempt, same day:** the injection was then written as a
`for p in … "$(git rev-parse --show-toplevel)/…"; do … exit 0; done` loop to
also find a profile from a subdirectory. In headless mode every skill using it
**aborted silently — 0 turns, 20 ms, empty result, no error** (a failed or
disallowed `!` command aborts the whole invocation before the model sees it).
Replaced by `cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md
2>/dev/null || echo "NO LAB PROFILE…"` — plain commands only; `/lab:tldr` went
from 0 turns to a correct recap. Lesson: keep `!` injections to simple
commands with no substitution, loops, or `exit`, and test every skill once
with `claude -p "/lab:<skill>" --output-format json` — `num_turns: 0` is the
signature of this failure. Cost accepted: a session started in a subdirectory
won't find the profile and falls back to defaults (and says so).
**Known residual, not yet chased further:** the repo this
plugin was extracted from keeps its own specialised copies of five skills, so
an improvement to a procedure has to be made in both places.

### Deliberately not built
A numeric tool registry, an MCP server, an API agent loop, hooks that force
plan mode. None has shown it is needed; revisit after two projects of use.

## All skills

<!-- skills:start -->

**Reflexes**

| Command | Arguments | What it does |
|---|---|---|
| `/big-job` | `[previous \| N jobs back \| the job's name]` | Back to the multi-step job we left: its phase checklist with current states, and the remaining phases numbered to resume. |
| `/go` | `[N \| N M … \| all \| next]   (nothing = resume what was interrupted)` | Proceed. /go 2 does item 2 of the last numbered list; bare /go resumes whatever was interrupted, no questions. |
| `/huh` | `<term, phrase, or "that last line">` | What does that mean? Three lines: the plain definition, what it meant here, a tiny example. |
| `/last` | `[N turns \| session \| <topic>]` | What just happened in this chat? Six short blocks: asked, did, result, files changed, left open, next. |
| `/progress` | `[process id \| task id \| label]   (none = everything running)` | How far along is a running job, and when does it finish? Percent, rate, remaining and a clock time, from a real signal. |
| `/rectify` | `<the correct fact, or what was wrong>` | Claude got something wrong. Pins the error, traces where it spread (numbers, files, decisions), fixes it. |
| `/update-context` | `"<the new fact or decision>"` | Something changed outside the session. Works out what it invalidates or unlocks, then records it. |
| `/where` | `<the thing> [--open]` | Where is that file? The exact path, one line on what it is, and how to open it. |
| `/your-take` | `[idk \| your lean or doubt \| the question]` | Undecided? Claude commits to a pick, gives the reasons that carry it and what would flip it, then a numbered list for /go N. |

**Start**

| Command | Arguments | What it does |
|---|---|---|
| `/lab:init` *(manual)* | `[optional: one line on what the project is for]` | Set the process up in a project: writes the profile (headline metric, the units that bind, where records go); optionally an Obsidian vault (Home, analysis and deck templates). |
| `/lab:run` | `[the question or idea]` | Work a question end to end: picks the right entry point and chains the stages. |
| `/lab:tldr` | `[optional: a stage or topic to scope the recap to]` | Where is the project? State of play read from its files, blocking item first, every open item priced. |

**When you have an idea**

| Command | Arguments | What it does |
|---|---|---|
| `/lab:apply-academia` | `<idea or paper> on <target/application>` | Port a proven paper or method under your constraints: gap in orders of magnitude, verdict per mechanism (adopt / adapt / offline-only / reject). |
| `/lab:derive-ansatz` | `[the problem, as a question]` | New problem, nothing built: limiting cases, an analogy with its breaking points, 2-4 candidate solution forms, each with a kill test. |
| `/lab:draft-ideas` | `<problem or theme> [--n 12] [--wild]` | Many ideas fast, through forced lenses; cheap cull; top three with their first test and its price. |
| `/lab:prototype` | `<the idea> [--stage poc\|prototype\|mvp] [--budget <amount>] [--deadline <when>] [--team <n>] [--build]` | What would this idea take? One-page brief: riskiest assumption, PoC vs prototype vs MVP, smallest test, build / fake / skip, needs, effort, kill criteria. |

**Knowing what exists**

| Command | Arguments | What it does |
|---|---|---|
| `/lab:explore-and-report` | `<the thing to explore> [--depth scan\|read\|deep] [--survey]` | Research something external and file a sourced report: what it is, ups and downs in your units, what to try. |
| `/lab:novelty-claim` | `<the idea, as one sentence> [--depth scan\|standard\|thorough]` | Is it actually new? Logged search, nearest-neighbour table, claim wording you can defend. |

**Deciding**

| Command | Arguments | What it does |
|---|---|---|
| `/lab:challenge-design` | `[the choice to challenge]` | Challenge an existing choice from scratch: survives, replaced, or undecidable without a measurement. |
| `/lab:record-decision` | `[the decision]` | Log a choice and why, including the first attempt that was wrong, with its numbers. |
| `/lab:rule-stress-test` | `<the rule text, or the file/section containing it> [--adversary student\|pro\|lawyer]` | Red-team a rule, rubric or reward: cheapest exploit, who it favours, whether it can be enforced, minimal patches. |

**Trusting a result**

| Command | Arguments | What it does |
|---|---|---|
| `/lab:ablation-plan` | `<the result or effect to explain>` | The fewest runs that tell the competing explanations apart, predictions written down first. |
| `/lab:integrity-audit` | `<pipeline, dataset, backtest, or result to audit>` | Is the number measuring what it claims? Leakage, lookahead, survivorship, test-set tuning, flattering simulators. |
| `/lab:perf-investigation` | `<what is slow / too big / too expensive>` | Slow, too big, too costly: measure first, find where the cost really is, change one thing, re-measure. |
| `/lab:repro-check` | `<the result, report, or number to check>` | Can this number be regenerated from what is on disk? Command, code version, inputs, seed, environment. |
| `/lab:stage-report` | `[the stage or experiment that just finished]` | Close an experiment: the numbers, what was falsified, what broke, what it unblocks. |
| `/lab:stale` | `[--docs] [--reports] [--code] [path]   (none = all three)` | What has gone stale? Dead references, overtaken docs and reports, lying status rows, undeclared imports, each with evidence and a fix price. |


**Keeping the docs current**

| Command | Arguments | What it does |
|---|---|---|
<!-- skills:end -->
