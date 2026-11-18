---
name: record-decision
description: Append a design decision to the project's decisions log in a fixed lightweight format (Decision / Why, optional constraint-risk-residual blocks, and the corrected-first-attempt convention), and check whether it also belongs in an upstream project's log. Use whenever a choice is made, reversed, explicitly rejected, or survives a challenge — anything a future session might otherwise re-litigate without the original reasoning. Generic version — if the project has its own skill named record-decision, use that one instead.
argument-hint: [the decision]
metadata:
  group: decide
  phrase: "Log a choice and why, including the first attempt that was wrong, with its numbers."
---

# Record a decision

**Decision to record:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults: decisions in docs/lab/decisions.md (create it with a trailing '## Open / not yet decided' section), no upstream. Say in one line that defaults are in use and that /lab:init would fix it."`

Working contract: [contract.md](../../reference/contract.md).

The test for whether to record: might a future session (human or Claude)
otherwise re-litigate this, or silently undo it, without knowing why it was
chosen? Decision logs record *why*, so a challenge can be informed rather than
ignorant. **They are not a list of things that can't change** — an entry means
the next person gets to argue against the real reasoning instead of a guess.

## Where it goes

| Kind of change | File |
|---|---|
| How this project (or one track of it) builds something | that project's / track's decisions file, per the profile |
| Something that changes what an **upstream** named in the profile does, allows, or buys | the upstream's log — and flag any sign-off it needs |
| Both — a local finding that changes a real upstream choice | **both**: local records the evidence, upstream records the consequence |

Don't push upstream a decision that's only about how an experiment is built.
Don't keep only locally a finding that changes the real project.

**No matching track.** If the decision belongs to no existing track's stated
question (it is about a different question that a track merely consumes),
say so and propose opening a new track folder (the name and the question are the user's); until it exists, record it under
`Open / not yet decided` in the nearest track with the line *"no track of
its own yet — move this entry there when it has one."*

## Format

Append to the end of the entry list, **before** the
`## Open / not yet decided` section. Never rewrite or delete an entry that has
merely been superseded — add the new one and say what it replaces.

```markdown
### <Title, written as a statement of the choice, not a topic>
**Decision:** what was chosen, concretely. Name the actual file, function,
parameter, or value where one exists.
**Why:** the reasoning, including what the alternative was and what it would
have cost. One short paragraph — if it needs three, it is probably two
decisions.
```

Optional blocks, when they apply:
- `**Constraint attached to this decision:**` — what must stay true for it to
  remain valid.
- `**Operational consequence:**` — what this forces elsewhere.
- `**Risk accepted, and its mitigation:**`
- `**Known residual, not yet chased further:**` — an imperfection left
  deliberately, so nobody thinks it went unnoticed.
- `**Would be reopened by:**` — the measurement or event that falsifies it.

Undecided things go under `## Open / not yet decided` as a bullet: the
question, the current lean, and the measurement (with price) that would settle
it — mirrored into the open-questions ledger.

### The corrected-first-attempt convention — the valuable part

When the first approach was wrong and got fixed, record the wrong one too:

```markdown
**First attempt, corrected after <a diagnosed divergence / feedback>:** what
was tried, what it actually did (with the numbers), and the root cause. Then
the right fix and why it was right.
```

or, for something tried and abandoned:

```markdown
**Rejected first attempt, for the record:** ... Left as a cautionary note:
<the generalisable lesson>.
```

This stops the same wrong idea being retried, which a bare statement of the
final answer never does. Include the concrete numbers that showed it was wrong
("violations went from 0.000 to 25.227"), not "it didn't work."

## Writing mathematics — terse, every symbol's provenance labelled

**Symbol table first, then numbered steps, then the result.** Nothing else.
Every symbol carries a tag: **derived** / **measured** (what ran, where the
data is) / **sourced** (cited, URL verified) / **assumed** (*say so in that
word*).

- An assumed number and a sourced number must not look alike.
- Derivation as numbered lines, one step each, not prose.
- **State what cancels** — it says what the answer does *not* depend on.
- **Significant figures are a claim.** ~240 ms off an assumed input, not 239;
  give the sensitivity (`t ∝ 1/√μ`, ±16% over the plausible range).
- Give the sensitivity, not the algebra — that is what a reader acts on.

## Hard rules

- **Numbers, not adjectives.** "Converges in ~0.35 s vs ~560 s" beats "much
  faster." An entry without a measurement is usually an untested opinion —
  say so if that's what it is.
- **Name the file or parameter** the decision lives in.
- Keep entries short. The log is read in bulk at the start of a session.
- If the decision came from research, file the source via
  `lab:explore-and-report` and link the report rather than restating it.
- If the decision *overrides* something upstream says, note that explicitly
  and say why the situations differ — otherwise someone will later "fix" the
  divergence.
