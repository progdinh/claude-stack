---
name: prototype
description: Turn a freshly proposed idea into a one-page feasibility brief in minutes — the riskiest assumption, which stage it actually needs (PoC / prototype / MVP), the smallest test of it, what to build vs fake vs skip, what it needs (skills, parts, data, compute, people, permissions), a rough time and cost with provenance, acceptance and kill criteria, and the next command to run. Use when an idea is being proposed or pitched and the question is "what would this take", "is this doable", "what's the quickest way to try it", "scope this", or "poc / prototype / mvp for X". Produces a brief, not code, unless --build is given.
argument-hint: <the idea> [--stage poc|prototype|mvp] [--budget <amount>] [--deadline <when>] [--team <n>] [--build]
metadata:
  group: idea
  phrase: "What would this idea take? One-page brief: riskiest assumption, PoC vs prototype vs MVP, smallest test, build / fake / skip, needs, effort, kill criteria."
---

# Prototype brief

**Idea:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Fine for this skill — an idea may not have a project yet. Use generic currencies (time, money, people) and say so in one line."`

Working contract: [contract.md](../../reference/contract.md) §6 — the cheap
version that answers the question today beats the faithful one next month.

## Flags
| Flag | Meaning | Default |
|---|---|---|
| `--stage` | force a stage instead of letting step 2 choose | chosen in step 2 |
| `--budget` | money ceiling | profile's, else "student budget" — state the assumption |
| `--deadline` | when it must exist | none |
| `--team` | how many people can work on it | 1 |
| `--build` | after the brief, go on to build it (starts in planning mode) | off — brief only |

## The three stages — they answer different questions

| Stage | Question it answers | Looks like | Thrown away? |
|---|---|---|---|
| **PoC** | *Does the risky part work at all?* | one script / one breadboard / one notebook testing ONE assumption | yes |
| **Prototype** | *Does the whole thing hang together?* | end-to-end path, everything non-essential faked or hard-coded | mostly |
| **MVP** | *Will a real user actually use it?* | smallest version a real person can use unsupervised | no — it's v0 |

The most common mistake is building a prototype when a PoC was needed (the
risky part was never isolated), or an MVP when nobody has checked the risky
part works.

## Procedure — ten minutes, one page

### 1. The idea in one line, and who it's for
"<Thing> that lets <who> do <what>, judged by <outcome metric>." If it can't
be said in one line, say which half is unclear — that's the first finding.

### 2. Find the riskiest assumption → that picks the stage
List the 3–5 things that must be true for this to work (technical,
physical, economic, legal, human). Rank by *likelihood of being false ×
cost if it is*. The top one decides:
- it's a **technical/physical unknown** → **PoC** of exactly that;
- the parts are known but their **integration** is the doubt → **prototype**;
- it all plausibly works and the doubt is **whether anyone wants it** → **MVP**.

### 3. The smallest test of that assumption
What is built, what is measured, the number that means "go" and the number
that means "stop". In the profile's units where they apply. If a simulator,
a spreadsheet, or a back-of-envelope limit case can answer it, that beats
building anything — check the limits first (as the key parameter → 0 and → ∞).

### 4. Build / fake / skip
| Part | Build | Fake (how) | Skip |
Everything not touching the riskiest assumption is faked (hard-coded values,
a recorded file instead of a live feed, a human behind the curtain, an
off-the-shelf module) or skipped. Be explicit — this table is where scope is
actually controlled.

### 5. What it needs
- **Skills** — and which the team has vs must learn (learning time is cost).
- **Parts / hardware** — rough lines with prices tagged *assumed* unless
  fetched.
- **Data** — exists? licensed? how much? who labels?
- **Compute / services / credits** — and whether existing allocations cover it.
- **People / partners / permissions** — access, sign-offs, anything
  regulated (money, personal data, minors, radio, batteries, trading) →
  flag for proper review, don't wave through.
- **Existing assets** — what in this repo (or a sibling one) already does part
  of it. Look before listing anything as "to build".

### 6. Time and cost, honestly
A range, not a point: optimistic / likely / pessimistic, in person-days and
money, each figure tagged **assumed** unless sourced. Name the one item most
likely to blow the estimate. If `--deadline` or `--budget` is given, say
whether the *likely* case fits, and what to cut if not.

### 7. Acceptance, out of scope, kill
- **Done means:** 2–4 checkable criteria.
- **Out of scope:** the tempting adjacent things that will NOT be done.
- **Kill it if:** the result that means stop — decided now, before sunk cost
  argues otherwise.

### 8. What it unlocks, and the next command
If it works: the next stage and what it would need. Then the single next
command: `/lab:derive-ansatz` (the core is genuinely unsolved),
`/lab:apply-academia` (it rests on a paper), `/lab:explore-and-report`
(someone has probably built this), `/lab:rule-stress-test`,
or — with `--build` — planning mode.

## Output
One page, written to `<lab dir>/ideas/<slug>-brief.md` (and a row appended to
`ideas.md` if it exists). Terminal: the template below, filled, then stop.

```
IDEA        <one line>
RISKIEST    <the assumption>            → STAGE: PoC | prototype | MVP
TEST        <what is built / measured>  go: <number>   stop: <number>
BUILD       …      FAKE  …      SKIP  …
NEEDS       skills … · parts ~… (assumed) · data … · compute … · people/permissions …
EFFORT      <opt / likely / pess> person-days · ~<money> (assumed)   risk: <the one item>
DONE WHEN   …
NOT DOING   …
KILL IF     …
NEXT        /lab:<command> …
```

## Guards
- **Brief, not build.** Without `--build`, write no code. With it, the brief
  becomes the input to planning mode — it does not replace the plan.
- **Ten minutes, one page.** If it needs more, the idea needs
  `/lab:derive-ansatz`, not a longer brief.
- **Every estimate is tagged assumed** unless there's a source. A confident
  number invented on the spot is worse than a range.
- **Check it hasn't been done** — decisions log, ideas file, derivations index.
- Don't talk the user out of an ambitious idea; find the cheapest way to learn
  whether it's alive.
