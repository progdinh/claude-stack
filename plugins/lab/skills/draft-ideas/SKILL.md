---
name: draft-ideas
description: Fast divergent ideation before any derivation — generate many candidate ideas for a problem using forced lenses (invert the constraint, delete a component, steal from another field, 10x cheaper, move the work elsewhere…), cull them cheaply by limiting case and cost, and hand the best two or three to derive-ansatz. Use for "brainstorm", "give me ideas", "what could we try", "draft some directions", or when a problem is still too vague to derive on. Produces a ranked, filed idea list — not designs.
argument-hint: <problem or theme> [--n 12] [--wild]
metadata:
  group: idea
  phrase: "Many ideas fast, through forced lenses; cheap cull; top three with their first test and its price."
---

# Draft ideas

**Theme:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/ and generic currencies (time, money, memory, bytes moved, energy, the project's outcome metric). Say so in one line; suggest /lab:init."`

Flags: `--n <k>` how many to generate (default 12). `--wild` relax house rules
for generation only (flag every idea that breaks one).

Pipeline position: **draft → derive → explore → challenge → record.** This is
the wide end of the funnel: quantity first, judgement second, and the two are
kept in separate steps on purpose.

## 1. Frame — two lines, no more
The need in one sentence, and the binding currency from the profile. If the
theme is a solution in disguise ("add a cache"), restate it as the need
("p99 under load").

## 2. Diverge — one idea per lens, then free ones
Don't evaluate yet. One line each, concrete enough to picture:

| Lens | Question |
|---|---|
| Invert | What if the binding constraint were the *feature*? |
| Delete | Which component could be removed entirely, and what would have to be true? |
| Move | Do the work earlier / later / elsewhere (compile time, training time, the other chip, the client, the organiser)? |
| Steal | What field already solved this shape (control, finance, games, compilers, biology, logistics)? |
| 10x cheaper | What would you build with a tenth of the budget? |
| 10x less data / time | Same, for the other scarce thing. |
| Make it a rule | Could a rule, interface, or default remove the problem instead of solving it? |
| Known-vs-learned | Which part is exact and analytic, and is currently being learned or guessed? |
| Timescales | Split fast from slow — does each half become easy? |
| Opposite of the incumbent | Whatever is done now, do the reverse. |
| Ludic / wow | The version someone would stop and watch. |

Then add free ideas until you reach `--n`.

## 3. Cull — cheap filters only, 30 seconds per idea
- **Limit check:** does it do something sensible as the key parameter → 0 and
  → ∞? Dead if not.
- **Order-of-magnitude cost** in the binding currency: fits / 10× over /
  1000× over.
- **House rules:** does it break one? (With `--wild`, mark rather than kill.)
- **Already tried?** Check the decisions log and derivations index.

Keep the kills in the file with the reason — a killed idea on record is what
stops it coming back.

## 4. Rank the survivors
By **(expected effect on the outcome metric) ÷ (price of the first test that
would tell)**. Not by elegance. Give the first test and its price for the top
three.

## 5. File and hand off
Append to `<lab dir>/ideas.md` (create if missing): date, theme, the table
(idea · lens · cull result · first test · price · status). Top two or three →
suggest `lab:derive-ansatz` on each; ideas sourced from a paper →
`lab:apply-academia`. Don't start deriving inside this skill.

## Guards
- Ideas are labelled **intuition**, never claim. Nothing here is a decision.
- No idea gets more than three lines. Depth belongs to the next stage.
- If every idea is a variation of the incumbent, say so and run the lenses
  again — that is the failure this skill exists to catch.
- One sitting, and a short one.

End with: top three, their first tests and prices, and the file path.
