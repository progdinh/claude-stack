# Lab profile — <project name>

> Read by every `lab:` skill. Keep it under ~60 lines: it is injected into
> each skill invocation. Written by `/lab:init`; edit freely.

## What this project is for
<one or two sentences: the question it answers or the thing it ships>

## Headline metric — the outcome, not the proxy
- **Outcome that counts:** <e.g. closed-loop lap time · p99 latency under
  production load · monthly cloud bill · task completion rate>
- **Tempting proxies that must never be the headline:** <e.g. validation
  loss, parameter count, benchmark score, test coverage>

## Currencies — the units that bind here
| Unit | Where it binds | Current budget / ceiling (provenance) |
|---|---|---|
| <ms> | <what latency, measured where> | <240 ms — derived, see docs/…> |
| <€ / month or per unit> | <…> | <…> |
| <KB / MB> | <peak working set, bundle size, RAM…> | <…> |
| <…> | | |

If a choice can't be tied to one of these, it is serving a habit, not a
constraint.

## Paths
| Record | Path |
|---|---|
| Layout | <single-track · or multi-track: each `<track>/` has its own set below> |
| Derivations | `<docs/lab/derivations/>` + `README.md` index |
| Explorations | `<docs/lab/explorations/>` + `README.md` index |
| Decisions | `<docs/lab/decisions.md>` (ends with `## Open / not yet decided`) |
| Stage reports | `<docs/lab/reports/>`; raw outputs under `<artifacts/sNN_*/>` |
| Open-questions ledger | `<docs/lab/open.md>` |
| Live hypotheses (H1, H2, …) | `<CLAUDE.md or docs/lab/hypotheses.md>` |
| Roadmap / stage status | `<docs/roadmap.md>` |
| Optional: BOM · rules/regulations · ideas · partners | `<hardware/bom.md>` · `<docs/regulations/>` · `<docs/lab/ideas.md>` · `<docs/lab/partners/>` |

## Upstream
<Repos or documents whose decisions this project feeds, and the rule for when
a finding must be written there too. "None" is a fine answer.>

## House rules — hard constraints
- <e.g. budget ceiling per unit, banned inputs/dependencies, "no cloud at
  inference", licence constraints, regulatory limits>

## How things are run
<the one command pattern: `uv run python -m pkg.mod`, `pnpm test`, `cargo run`…>
