---
name: novelty-claim
description: Establish, with a logged and honest literature search, whether an idea is actually novel before the word goes on a slide, a paper, a grant, or a pitch — record the queries run and the depth read, tabulate the nearest neighbours and exactly what each does and does not do, locate the gap, and produce defensible claim wording plus what would invalidate it. Use for "is this novel", "has anyone done this", "what's the prior art", "related work", or before writing any claim of being first.
argument-hint: <the idea, as one sentence> [--depth scan|standard|thorough]
metadata:
  group: know
  phrase: "Is it actually new? Logged search, nearest-neighbour table, claim wording you can defend."
---

# Novelty claim

**Idea:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/. Say so in one line; suggest /lab:init."`

An absence claim is the hardest kind to support: "I found nothing" is only as
strong as the search. So the search itself is the deliverable.

`--depth`: **scan** ≈ 5 queries, abstracts (orientation only — never enough to
claim novelty). **standard** (default) ≈ 15 queries, nearest neighbours read
at method + results depth. **thorough** ≈ 30+ queries, citation-chasing both
directions, venues enumerated.

## Procedure

### 1. Decompose the idea into its claim components
Most "novel" ideas are a *conjunction*: A applied to B under constraint C
judged by metric D. Write the components. Novelty almost always lives in the
conjunction — each part alone usually exists.

### 2. Search, and log every query
For each component and each pair: the field's own vocabulary **and the
neighbouring fields' vocabulary** for the same thing (the most common way to
miss prior art is searching in your own dialect). Log: query · where · date ·
hits worth opening. Chase citations forward and backward from the best hit.
Name the 2–3 venues where this would have been published and check their
recent proceedings directly.

### 3. Nearest-neighbour table
| Work (verified URL) | Has A? B? C? D? | What it does | What it does NOT do | Depth read |

Be strict in "does NOT do" — read the method and results, not the abstract.
The closest neighbour deserves a paragraph: it is the paper a reviewer will
cite against you.

### 4. Locate the gap and classify it
- **New conjunction** of known parts — the usual honest answer.
- **Method transfer** into a domain where it hasn't been used.
- **New evaluation** — judging a known thing by the outcome instead of the proxy.
- **Negative / boundary result** — "no formulation fits budget X; here's the wall".
- **Actually new mechanism** — rare; demand more search before believing it.
- **Not novel** — found. Say so plainly; cite it; this just saved months.

### 5. Claim wording
Write the strongest sentence the search supports, e.g. *"To our knowledge the
first in the open literature to … (search: N queries, M venues, date)."*
Note what is **uncitable but certainly exists** (proprietary industry work) and
phrase around it. List what finding would invalidate the claim.

### 6. File
`<explorations dir>/novelty-<slug>.md` + index row, including the full query
log. Re-run before any submission — novelty decays.

## Guards
- **No fabricated or unverified citations.** Recalled-but-unverified works are
  listed as *recalled, not verified* and count as **unsearched**.
- A scan can find prior art; it can never establish novelty. Say which depth
  was run in every sentence that uses the word.
- Don't soften a "not novel" finding. Reframe the contribution instead.

End with the four-part TL;DR: the claim wording, the nearest neighbour, the
search depth, the price of going one level deeper.
