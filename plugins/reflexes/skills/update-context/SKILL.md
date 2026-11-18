---
name: update-context
description: The user is giving Claude a NEW fact, decision, or change of premise that happened outside the session — "now the car is 1/10 scale", "we got the sponsor", "the deadline moved", "we dropped X", "I decided Y". Not a correction of something Claude said (that is /rectify). Restate the fact, sanity-check it, work out what it invalidates or unlocks across the project's records (decisions, derived numbers, budgets, hypotheses, plans, memory), then record it — immediately if it's trivial and nothing depends on it, with an impact list and explicit confirmation if it has consequences, and with a flag first if it contradicts the evidence or looks like a slip.
argument-hint: "<the new fact or decision>"
metadata:
  group: reflex
  phrase: "Something changed outside the session. Works out what it invalidates or unlocks, then records it."
---

# update-context — a new premise from outside the session

**New context:** $ARGUMENTS

Things change between sessions: a part gets chosen, a rule gets rewritten, a
partner says yes, the user changes their mind in the shower. The job here is to
make the project's *record* and my *working assumptions* match the new reality
— and to say clearly what that reality now breaks.

## 1. Restate it — one line
"As of <today's date>: <the fact>, replacing <what was assumed before, with
where that was written>." If it isn't clear what it replaces, say what I
*think* it replaces and check. Note the **kind**: a decision the user made · a
fact about the world · a constraint (budget, deadline, rule) · a scope change ·
a preference.

## 2. Sanity-check — seconds, not minutes
- **Internally consistent?** Units, magnitudes, dates that make sense.
- **Consistent with the record?** What do the project's files currently say?
- **Physically / financially / logically possible** given the project's other
  hard constraints (the profile's house rules, the budget, the hardware)?

Most updates pass instantly. If it fails, go to step 5 **before** recording
anything.

## 3. Impact — what does this invalidate, and what does it unlock?
Walk the record (lab profile, `CLAUDE.md`, decisions log, roadmap, live
hypotheses, derivations, reports, BOM, ledger, memory):

| | |
|---|---|
| **Invalidated** | decisions whose *Why* no longer holds · numbers derived from the old premise (give old → new where computable) · results measured under the old premise · plans/stages that no longer make sense |
| **Needs re-measuring** | what can't be recomputed and must be re-run — with a price |
| **Unlocked** | options that were closed and now aren't; ledger items this answers |
| **Untouched** | what survives, and why — this is as useful as the rest |

Scale-type changes (size, budget, rate, count) propagate through every
derived quantity: follow the formulas, don't eyeball it.

## 4. Triage — this decides whether to ask

**Trivial → just record it, then say so in one line.**
All of: nothing derived changes; no decision's reasoning breaks; nothing needs
re-measuring; it's a preference, a name, a date nobody depends on, a contact,
a status. Write it where such facts live (profile / `CLAUDE.md` / memory) and
report: `Recorded: <fact> in <places>. Nothing downstream.`

**Consequential → show the impact, then ALWAYS ask before changing anything.**
Any of: a derived number moves; a decision or hypothesis is invalidated; a
result needs re-measuring; a budget, scope, or deadline shifts; upstream is
affected. Present:

```
New         <the fact>            replaces  <the old premise, where it was written>
Invalidates
  - <decision / number / result>: why, and old → new if computable
Re-measure  <what, and the price>
Unlocks     …
Untouched   …
Proposed    1. record the fact in <files>
            2. mark <entries> superseded (not deleted), dated, pointing here
            3. add <re-measurements> to the ledger with prices
```

then ask once — apply all / apply some / just remember it for this session.
Use the question tool if available. Do not edit while waiting.

Recording rules: **supersede, never erase** — old decisions stay, marked
superseded with the date and the new fact, so the reasoning trail survives.
Results measured under the old premise get a visible "measured at <old
premise>" label rather than being deleted. A changed premise is a decision →
`record-decision` (the project's own, else `lab:record-decision`), upstream
too if the profile names one.

## 5. If it looks like a slip — flag it, respectfully, first

Only for a real conflict: it contradicts a measurement, the hard constraints,
arithmetic, physics, or something the user said earlier. Not for being
ambitious or surprising — ambitious is fine.

```
⚑ Before I record this — it conflicts with:
  - <the specific evidence: file:line, the number, the constraint>
  - <what would follow if taken literally — the consequence that looks off>
Did you mean: <the most likely intended value / reading>?  Or is this a real
  change — in which case it also means <the biggest knock-on>.
```

Typical slips worth catching: a unit or ratio that's off by a factor (1/2 vs
1/12, ms vs s, k€ vs €), a figure that breaks a hard budget, a date in the
past, a name that matches two things. Record nothing until answered. If the
user confirms, it's real: proceed via step 4 and note it was confirmed over
the conflict. One flag, not an argument.

## Rules
- The user's word **is** the evidence for their own decisions, plans, and
  preferences — never ask them to justify a decision, only to confirm it when
  it has consequences or looks like a typo.
- Don't start re-doing invalidated work. List it, price it, stop.
- If the update is really a correction of something *I* said, say so and
  handle it as `/rectify`.
- Save standing facts to memory (if this session has one) so the next session
  starts from the new premise.
- After recording, resume whatever was in progress — under the new premise.
