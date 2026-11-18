---
name: rectify
description: The user is correcting something Claude said or did — a wrong fact, number, assumption, name, or interpretation. Pin down exactly what was wrong, check the correction against the evidence, trace everywhere the error propagated in this session (files written, numbers derived from it, decisions, memory), then fix it — trivially and immediately if nothing depends on it, with an impact list and explicit confirmation if something does, and with a respectful flag first if the correction itself contradicts the evidence. Use for "/rectify …", "that's wrong", "no, it's actually X", "you got X wrong", "correct that".
argument-hint: <the correct fact, or what was wrong>
metadata:
  group: reflex
  phrase: "Claude got something wrong. Pins the error, traces where it spread (numbers, files, decisions), fixes it."
---

# rectify — the user is correcting me

**Correction given:** $ARGUMENTS

The default assumption is that the user is right: they know their project,
their hardware, their organisation and their intent better than I do. The job
is to fix the error *and everything it touched* — not to defend it, and not to
silently patch one sentence while the wrong number lives on in three files.

## 1. Pin it — one line each
- **I said:** quote my wrong statement, with where it was (message, file:line).
- **Actually:** the corrected fact, in the user's terms.
- **Kind:** a fact about the world · a number · an assumption I made · a
  misreading of what was asked · a name/label · something I did, not said.

If I can't find what I said that this corrects, say so and ask which statement
is meant — don't guess and "fix" something else.

## 2. Check the correction against evidence — briefly
What do the files, the measurements on disk, or the sources say? One or two
quick reads at most. Three outcomes:

- **Consistent with the evidence (or there is no evidence either way)** →
  accept it. The user's word is the evidence for anything about their own
  project, plans, hardware, or preferences.
- **I was wrong AND the record is wrong too** → say so: the correction applies
  to the files as well, not just to the chat.
- **The correction contradicts solid evidence** → go to step 5 before
  changing anything.

## 3. Trace the blast radius — in this session and in the record
Where did the wrong thing go?
- statements I made later that relied on it;
- **numbers derived from it** (recompute them — give old → new);
- files I wrote or edited (reports, decisions, derivations, code, configs);
- conclusions, verdicts, or recommendations that would now change;
- memory entries.
List it. If nothing depends on it, say "nothing downstream".

## 4. Triage — this decides whether to ask

**Trivial → just fix it, then say so in one line.**
All of: nothing derived from it changes; no verdict, decision, or
recommendation changes; the fix is a wording/name/typo/label or a single
value with no dependents; it's reversible. Apply it everywhere it appears and
report: `Fixed: X → Y in <places>.`

**Consequential → show the impact, then ALWAYS ask before changing anything.**
Any of: a derived number moves; a verdict or decision would change; a filed
record (decision, report, derivation) needs amending; code or config changes;
something upstream is affected. Present:

```
I said      …
Actually    …
This changes
  - <number>: old → new
  - <file>: what would be amended
  - <verdict/decision>: how it moves
Doesn't change
  - what survives, and why
Proposed    the edits, in order
```

then ask once — apply all / apply some / leave the record and just note it.
Use the question tool if available. Do not start editing while waiting.

When amending records: **never silently rewrite history.** Decisions and
reports get the corrected-first-attempt treatment — the wrong value, what it
led to, and the correction, dated — so the next reader doesn't act on the
stale number *or* wonder why it changed.

## 5. If the correction looks wrong — flag it, respectfully, first

Only when it contradicts something solid: a measurement on disk, a verified
source, arithmetic, physics, or what the user themselves said earlier. Not
when it merely surprises me.

```
⚑ Before I change this — it conflicts with:
  - <the specific evidence, with file:line / source / the calculation>
  - <what would follow if the correction is true — the consequence that looks off>
Possible readings: <the 1–2 ways both could be true — different unit, different
  part, a plan vs. the current state, I misunderstood the correction>
Which is it?
```

Change nothing until answered. If the user confirms, they're right: apply it
(via step 4), and record that it was confirmed over contrary evidence, and
what that evidence was. One flag, not an argument — don't re-raise it.

## Rules
- No grovelling, no long apology. One line owning the error, then the fix.
- Don't over-correct: fix what was wrong, not adjacent things I now feel
  unsure about. If the error makes me doubt something else, list it under
  "worth re-checking" with a price — don't go and re-do it.
- If the same kind of error is likely to recur (a unit, a naming convention, a
  standing fact about the project), offer to save it to memory / the project's
  profile so it doesn't.
- After the fix, resume whatever was in progress.
