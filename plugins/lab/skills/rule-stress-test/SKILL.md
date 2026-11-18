---
name: rule-stress-test
description: Red-team a draft rule, regulation, scoring rubric, reward function, or competition format — find the cheapest way to win or comply while defeating its intent, check which participants it silently favours, check what it makes unmeasurable or unenforceable, and propose the smallest rewording that closes each hole. Use when drafting or reviewing competition regulations, scoring systems, RL reward shaping, KPIs, acceptance criteria, policies, or any rule someone will optimise against.
argument-hint: <the rule text, or the file/section containing it> [--adversary student|pro|lawyer]
metadata:
  group: decide
  phrase: "Red-team a rule, rubric or reward: cheapest exploit, who it favours, whether it can be enforced, minimal patches."
---

# Rule stress test

**Rule under test:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/. Say so in one line; suggest /lab:init."`

Anything that is scored will be optimised, and the optimiser doesn't read the
preamble. A rule is a reward function for humans; the same failure modes apply
(specification gaming), and the same fix: find the exploit before the
participants do.

`--adversary`: **student** (default — clever, time-rich, budget-poor),
**pro** (money and tooling), **lawyer** (argues the letter of the text).

## 1. State the intent separately from the text
One sentence: what behaviour is this rule *for*? If the intent isn't written
anywhere, that is the first finding — an unstated intent can't be defended in
a dispute. Quote the rule text exactly, with its file and article number.

## 2. Attack it — in character
For each, the **cheapest** strategy, its cost, and what it wins:
- **Letter vs spirit:** satisfy every word while defeating the purpose.
- **Undefined terms:** every noun and threshold without a definition or a
  measurement method is a hole ("trained model", "onboard", "autonomous",
  "latency", "team member").
- **Move the work outside the boundary:** precompute, offload, do it before
  the clock starts, do it in the part the rule doesn't cover (the wrapper
  around the model, the pit crew, the organiser's own infrastructure).
- **Degenerate optima:** do nothing, go slow, abstain, farm the easy points,
  exploit a floor or a cap, tie-break abuse.
- **Collusion and sacrifice:** two entrants cooperating; an entry that exists
  to harm a rival.
- **Buy the win:** what does 10× the budget get? Is the advantage linear,
  capped, or winner-takes-all?
- **Information asymmetry:** who benefits from knowing the track / data /
  seed / schedule / organisers?
- **Infrastructure as a player:** location, network, hardware lottery, time
  zone, order of running.

## 3. Fairness — who does it silently favour?
By budget, prior experience, school resources, geography/latency, language,
access to hardware, team size. For each: advantage size, and whether that
advantage is *the thing the competition means to reward*. Favouring skill is
the point; favouring money usually isn't.

## 4. Enforceability
For each clause: how would a violation be **detected**, by whom, with what
instrument, at what cost, and what happens in a dispute? A rule nobody can
check is a suggestion. Prefer constraints enforced by construction
(organiser-supplied interface, fixed hardware, sealed executor, physical
isolation) over constraints enforced by inspection.

## 5. Second-order effects
What does this rule make teams *stop* doing that you wanted? What does it make
the dominant strategy? Is the winning entry one you'd be proud to showcase?

## 6. Patches — smallest first
Per hole: the minimal rewording or mechanism that closes it, what it costs
participants and organisers, and what new hole it might open. Sometimes the
right patch is to **delete the rule** and fix an interface instead.

## 7. File and hand off
`<lab dir>/rules/<slug>.md`: intent · text · exploit table (exploit · cost ·
payoff · severity · patch) · fairness table · enforceability table. Severity:
**breaks the competition / distorts it / cosmetic**. Rule changes are
decisions → `lab:record-decision`, and upstream if the profile names the
rulebook's repo. Unresolved holes → ledger with a price.

## Guards
- Attack the rule, not the people who wrote it.
- Every exploit needs a cost and a payoff — "someone could cheat" is not a finding.
- Don't pile on clauses: each patch must be weighed against the complexity it
  adds. A rulebook nobody can hold in their head gets gamed at the seams.
- Any money, prizes, tokens, or regulated activity (trading, betting, personal
  data, minors) → flag for qualified legal review; do not give legal advice.

End with the four-part TL;DR: the worst exploit and its price lead.
