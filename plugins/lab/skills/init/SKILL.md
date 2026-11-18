---
name: init
description: Bootstrap the lab research process in the current project — inspect the repo, draft a lab profile (docs/lab/profile.md) naming its headline metric, binding currencies, record paths, upstream and house rules, create the record folders with index files, and offer a short pointer in the project's CLAUDE.md. Run once per project, or again to refresh the profile.
disable-model-invocation: true
argument-hint: [optional: one line on what the project is for]
metadata:
  group: start
  phrase: "Set the process up in a project: writes the profile (headline metric, the units that bind, where records go); optionally an Obsidian vault (Home, analysis and deck templates)."
---

# Initialise the lab in this project

**User's note:** $ARGUMENTS

## Current state (injected)

```!
echo "project dir: ${CLAUDE_PROJECT_DIR}"
echo "--- existing profile:"; cat "${CLAUDE_PROJECT_DIR}/docs/lab/profile.md" 2>/dev/null || cat "${CLAUDE_PROJECT_DIR}/.claude/lab.md" 2>/dev/null || echo "(none)"
echo "--- top level:"; ls "${CLAUDE_PROJECT_DIR}" 2>/dev/null | head -40
echo "--- existing records:"; find "${CLAUDE_PROJECT_DIR}" -maxdepth 4 \( -name "decisions.md" -o -name "roadmap.md" -o -name "explorations" -o -name "derivations" -o -name "open.md" \) -not -path "*/node_modules/*" -not -path "*/.git/*" 2>/dev/null | head -20
```

Template: [profile-template.md](../../reference/profile-template.md).
Contract the profile plugs into: [contract.md](../../reference/contract.md).
Obsidian templates (step 5b): `${CLAUDE_PLUGIN_ROOT}/reference/obsidian/` — `Home.md`, `analysis.md`, `deck.md`.

## Procedure

### 1. Read the project before asking anything
README, CLAUDE.md, the manifest (`pyproject.toml`, `package.json`,
`Cargo.toml`, …), the docs folder, the last ~20 commits. You are looking for:
what the project is for; what it is judged by; what is scarce; how things are
run; whether it is one project or several tracks; whether it feeds another
repo.

### 2. Draft the profile — the two sections that matter most

**Headline metric.** The outcome that actually counts vs. the proxies that are
tempting to report instead. If the repo only ever reports a proxy, that is the
first finding — say so.

**Currencies.** The 3–6 units that genuinely bind *here*, each with where it
binds and the current budget with its provenance (measured / sourced /
derived / **assumed**). Do not paste a generic list: a web service binds on
p99 ms, cost per month and on-call hours; an embedded project on KB of SRAM,
ms of loop latency, euros of BOM and joules; a research codebase on GPU-hours
and wall-clock per experiment. A currency nobody can put a number on goes in
as `budget: not established` — that gap is itself useful.

### 3. Respect what already exists
If the project already has a decisions log, a roadmap, an explorations folder
or similar, **point the profile's Paths at them** — never create a parallel
set. Only fall back to `docs/lab/…` for records that have no home yet. In a
multi-track repo, say whether records are per-track (`<track>/docs/…`) or
shared.

### 4. Ask only what the repo can't answer
At most one round of questions, only for things that are genuinely the user's
call and change the profile: the headline metric if ambiguous, hard budget
ceilings, upstream repos, house rules (banned dependencies, licence or
regulatory constraints). Don't ask about paths or conventions you can infer.

### 5. Write
- The profile, from the template, under ~60 lines (it is injected into every
  `lab:` skill call). **Location: `docs/lab/profile.md`** — versioned with the
  docs and writable in every permission mode. (`.claude/lab.md` is also read
  by the skills, and an existing profile there is updated in place; but
  `.claude/` writes are permission-gated and blocked outright in headless
  runs, so it is not the default.)
- Missing record folders, each with a `README.md` index whose table header is
  ready for the first row: derivations
  (`Date | Problem | Ansätze | Outcome`), explorations
  (`Date | Topic | Source | Status` + a "Still to file" table).
- The decisions file if missing: a one-paragraph header, then
  `## Open / not yet decided` at the bottom.
- The ledger if missing: `| Item | Price | Raised by | Date | Status |`.
- **Offer** (don't do silently) to add a short section to the project's
  `CLAUDE.md` pointing at the profile and stating the two rules that change
  behaviour most: *implementation starts in planning mode with a challenge*,
  and *every step ends with a filed record plus the four-part TL;DR*.

### 5b. Obsidian vault (opt-in — ask once, alongside step 4)
Offer it when the repo has a `.obsidian/` folder, or the user mentions
Obsidian; otherwise skip silently. If accepted, **core plugins only, nothing
to install**:
- `Home.md` at the repo root from `reference/obsidian/Home.md` (entry point:
  a **Status** table, an **Analyses log**, links to the records). If one
  exists, add the missing sections; never overwrite.
- `templates/analysis.md` and `templates/deck.md` from `reference/obsidian/`
  (put them where the project keeps docs; `docs/templates/` by default).
- Conventions, written into the profile as a `## Vault` section of ≤6 lines:
  every analysis is a note in the reports folder made from the analysis
  template, its frontmatter carries a `headline` **with a number**; every
  analysis adds a row to Home's Analyses log and updates Status when it
  moves; decks (slides split by `---`, shown with *Start presentation*) go in
  `presentations/`; diagrams are Mermaid; figures go in `figures/`.
- Tell the user to open the repo root as a vault. Don't touch `.obsidian/`
  settings, and add `.obsidian/workspace*.json` to `.gitignore` if the user
  versions the vault.

`lab:stage-report` and `lab:record-decision` follow the `## Vault` section
when the profile has one.

### 6. If a profile already existed
Show a diff-style summary of what you would change and why; keep anything the
user evidently wrote by hand.

## Guards

- Don't invent budgets. An unknown ceiling is written as unknown.
- Don't reorganise the project's existing docs to fit the defaults.
- Don't commit. Leave the new files for the user to review.

End with a 5-line summary: headline metric, the currencies chosen, where
records will go, anything marked `not established`, and the suggested first
skill to run (`/lab:challenge-design` on the least-justified number in the
repo is usually a good opener).
