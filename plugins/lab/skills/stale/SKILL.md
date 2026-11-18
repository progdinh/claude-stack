---
name: stale
description: Find what has gone stale in a project — docs that cite files which no longer exist or have changed since, status tables and roadmaps that disagree with what is on disk, reports and decisions overtaken by later ones or measured under a premise that has since changed, numbers quoted in prose that differ from the constants in code, imports not declared as dependencies, scripts that no longer run. Report-only, each item with its evidence and the price of fixing it. Use for "/lab:stale", "what's out of date", "is this doc still true", "clean up the docs", before a handover, a release, or a write-up.
argument-hint: [--docs] [--reports] [--code] [path]   (none = all three)
metadata:
  group: trust
  phrase: "What has gone stale? Dead references, overtaken docs and reports, lying status rows, undeclared imports, each with evidence and a fix price."
---

# stale — what is no longer true

**Arguments:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/. Say so in one line; suggest /lab:init."`

Git tracks *versions*. This tracks **validity**: is this still true, and what
made it stale? Report-only — never delete, never rewrite; propose.

## 1. Mechanical pass — run the scanner
`python3 ${CLAUDE_SKILL_DIR}/stale_scan.py <root> [--docs] [--code]`
- **dead references** — a doc cites a path that isn't there. Triage each: a
  real rename/deletion (stale) vs a placeholder, an example, or a file that is
  *planned* (not stale — but say the doc should mark it as planned).
- **overtaken docs** — a cited file changed in git after the doc last did.
  Open the doc: does what it *says* about that file still hold? Most are fine;
  report only the ones that aren't.
- **undeclared imports** — code that can't run from a clean environment.
The scanner over-reports by design. **Never paste its raw output as findings**
— verify each before listing it.

## 2. Judgement pass — what no script can see
`--docs`
- **Status rows that lie**: roadmap / README / CLAUDE.md status vs what
  actually exists (artifacts, code, reports). The most common stale item.
- **Numbers in prose vs constants in code**: grep the doc's key figures
  against the source of truth.
- Instructions that no longer work (a command, a flag, a path in a how-to).

`--reports`
- A report or decision **overtaken by a later one** that doesn't point to it.
- Results **measured under a premise that has since changed** (a scale, a
  budget, a constant later corrected) and not labelled as such.
- Open items in the ledger / `Open / not yet decided` that were answered.
- Hypotheses whose status moved but whose statement didn't.

`--code`
- Scripts/entry points that no longer run: try `--help` or an import, cheaply.
- Code referencing names dropped elsewhere (a rename half-done).
- Keep it narrow: docs↔code disagreement and can't-run. **Not** a general
  dead-code or style hunt.

## 3. Report — one table, worst first

| # | Item | Why it's stale | Evidence | Fix | Price |
|---|---|---|---|---|---|

- Severity order: **misleads a decision** > **breaks a run** > **cosmetic**.
- Evidence is `file:line` on both sides of the disagreement.
- Fix is the smallest honest one: correct the line, mark superseded (dated,
  pointing at what replaced it), label "measured under <old premise>", declare
  the dependency. **Supersede, never erase.**
- Then the count the scanner raised vs the count that survived verification.
- End with a numbered list: fix all cosmetic ones in one go; each
  decision-affecting one separately. Fixing starts only on `/go N`.

## If the judgement pass keeps finding the same kind of thing
That is the signal to add a provenance header to records (`status`,
`depends_on`, `measured_under`, `superseded_by`) so it becomes mechanical.
Propose it with the count that justifies it — don't add it pre-emptively.
