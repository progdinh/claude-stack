---
name: bom-check
description: Build or audit a bill of materials with real, verified supplier prices — per-part price, supplier link, stock and lead time, second source, what each part displaces, and per-unit vs bulk totals against the budget.
disable-model-invocation: true
argument-hint: [--bulk [N]] [--detail "<what it's for>"] [--region EU|US|…] [--budget <amount>] [--file <existing BOM path>]
metadata:
  group: organise
  phrase: "Bill of materials with real fetched prices, stock, second sources, totals against budget."
---

# BOM check

**Arguments:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/. Say so in one line; suggest /lab:init."`

## Flags
| Flag | Meaning | Default |
|---|---|---|
| `--detail "<text>"` | what the BOM is for (e.g. "RC car", "validator node") — used to find the existing BOM or to draft one | infer from the profile |
| `--bulk [N]` | also price N units (price breaks, MOQ, shipping amortised, spares) | off; N = 10 if flag given bare |
| `--region` | supplier region for prices, VAT, shipping, customs | the profile's; else EU |
| `--budget` | per-unit ceiling to judge against | the profile's |
| `--file` | an existing BOM to audit instead of drafting | search the repo for one |

Anything in the arguments that isn't a flag is treated as extra `--detail`.

## Procedure

1. **Find or draft the part list.** Existing BOM first (`--file`, or search
   the repo). If drafting: list functions before parts (compute, sensing,
   actuation, power, structure, connectivity, consumables, tools) so nothing
   is forgotten — cables, connectors, fasteners, SD cards, chargers, and
   safety items are where BOMs lie.
2. **Price every line from a real supplier page, fetched now.** Record:
   part · exact model/SKU · supplier · URL · unit price incl./excl. VAT ·
   date checked · in stock? · lead time. Prefer distributors and the
   manufacturer's store in `--region` over marketplaces. **A price that wasn't
   fetched is labelled *assumed*.** Never invent a URL or a price.
3. **Second source.** For each line: an alternative supplier or a drop-in
   equivalent. Single-sourced and out-of-stock parts are the supply risk —
   flag them.
4. **What does it displace?** For any part proposed as a change: what it
   replaces, and the net effect on the total and on the profile's other
   currencies (grams, mW, mm, ms).
5. **Totals.** Per unit: subtotal, shipping, VAT, customs where relevant,
   **total vs `--budget`** with the margin. With `--bulk N`: price breaks and
   MOQs applied, shipping amortised, a spares allowance (state the %), total
   for N and effective per-unit.
6. **Risk notes.** Parts near end-of-life, parts with volatile pricing, parts
   whose specs are unverified, anything needing certification or with
   shipping restrictions (LiPo batteries, radio modules).
7. **Cheaper structure?** One pass of `challenge-design` thinking on the top
   two cost lines: is there a cheaper part class that satisfies the same
   constraint? Quote it with a price or don't mention it.

## Output
A BOM table in the file the profile names for it (else
`<lab dir>/bom/<slug>.md`), a totals block, a risks block, and the date — BOM
prices rot, so the date is part of the result. Decisions (a swapped part, a
changed budget) → `lab:record-decision`, and upstream if the profile names
where the real BOM lives.

## Guards
- Every price has a URL and a date, or the word *assumed*.
- Don't quote a marketplace listing as a stable supplier price without saying so.
- Don't silently change the design to hit the budget — propose, with the trade.

End with: total vs budget, the three biggest lines, the riskiest line, and
what would cut the most for the least.
