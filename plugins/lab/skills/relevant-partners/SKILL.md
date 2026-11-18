---
name: relevant-partners
description: Find and rank potential partners for a project — industrial sponsors, cash funders, compute or credit providers, academic labs, mentors — each verified from a public source, with what they could give, why they would care, the specific ask, and the evidence to bring.
disable-model-invocation: true
argument-hint: [--industrial] [--cash] [--compute] [--credits] [--academia] [--mentoring] [--region <where>] [--for "<project or ask>"] [--n 10]
metadata:
  group: organise
  phrase: "Verified potential partners: what they could give, why they would care, the specific ask, the evidence to bring."
---

# Relevant partners

**Arguments:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/. Say so in one line; suggest /lab:init."`

## Flags — each selects a kind of support; none given = all
| Flag | Looks for | The ask is usually |
|---|---|---|
| `--industrial` | companies whose product, hiring, or brand overlaps the project | hardware/kit, engineers' time, a challenge track, visibility deal |
| `--cash` | sponsors, foundations, grants, school/alumni funds, public programmes | a sum, tied to a named line in the budget |
| `--compute` | cloud/GPU providers, HPC centres, university clusters | GPU-hours or a node allocation |
| `--credits` | startup/education/research credit programmes (cloud, API, tooling) | credits via an existing programme — check eligibility rules |
| `--academia` | labs, chairs, research groups working on the same problem | co-supervision, a reading of the design, a joint paper, a venue |
| `--mentoring` | individuals with directly relevant experience | an hour, a review, a jury seat |
| `--region` | geographic focus | the profile's; else infer |
| `--for "<text>"` | the project or specific need | the profile's purpose |
| `--n` | how many to return per category | 10 |

## Procedure

1. **State what the project can offer before asking for anything.** Audience
   (who, how many, which schools), talent pipeline, a showcase for their
   product, open-source output, data, a research result, press. Partners fund
   their own goals. If there's nothing to offer yet, that's the finding.
2. **State the need in units.** Not "support" — "40 boards at about 15 € each",
   "2,000 GPU-hours before March", "a reviewer for the consensus design". Pull
   from the BOM, the ledger, the roadmap.
3. **Search, and verify every entry from a public source fetched now.** The
   organisation exists, does what you say it does, and the programme is
   current (dates, eligibility, region). For people: only public professional
   roles from public pages; no private contact details, no guessing emails.
   **Anything recalled but not verified is listed separately as *unverified
   lead*** — never mixed into the table.
4. **Rank by fit × likelihood ÷ effort**, not by prestige. A local company
   that hires from the school beats a famous one with no reason to reply.
   Existing relationships (profile, README, site) rank first.
5. **Per partner, write the row:**
   who · category · what they could give · **why they would care** (their
   incentive, in their terms) · the specific ask · evidence to bring (a
   number, a demo, a report from this repo) · warm path (who already knows
   them) · source URL · date checked.
6. **Conflicts and strings.** Exclusivity, IP or publication constraints,
   branding obligations, competitor clashes between sponsors, anything that
   would compromise independence (e.g. a sponsor who is also a participant).

## Output
`<lab dir>/partners/<slug>.md`: the offer, the need, one table per selected
category, unverified leads, conflicts, and the three to contact first with a
one-paragraph tailored pitch each (evidence, not adjectives). Follow-ups →
ledger.

## Guards
- No fabricated organisations, programmes, people, or URLs — ever.
- Don't draft or send outreach on the user's behalf unless asked.
- Programme terms change: every eligibility claim carries its date and link.
- Money from regulated or controversial sectors → flag for the board, don't decide.
