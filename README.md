# sevel-stack — Joseph's Claude Code stack

Two plugins plus two drop-in templates, as used at the hackathon.

## Install

```
/plugin marketplace add progdinh/claude-stack     # or a local path
/plugin install lab@sevel-stack
/plugin install reflexes@sevel-stack
```

| Plugin | What you get |
|---|---|
| `lab` | `/lab:run`, `derive-ansatz`, `draft-ideas`, `challenge-design`, `explore-and-report`, `record-decision`, `stage-report`, `tldr`, `prototype`, `novelty-claim`, `init`, … — a research process where every step leaves a filed, falsifiable, priced record. Guide: `plugins/lab/GUIDE.md`. |
| `reflexes` | `/reflexes:go`, `huh`, `last`, `progress`, `rectify`, `update-context`, `big-job`, `where`, `your-take`, `update-docs`. Short skills that read the conversation and answer briefly. |

**Guide (3 pages per language):** [English](docs/stack-guide.en.pdf) · [Français](docs/stack-guide.fr.pdf). The nine skills I use most come first.

Plugin skills are namespaced (`/lab:tldr`); copy a skill folder to `~/.claude/skills/` if you want the bare `/tldr`.

## Templates (not installable as plugins)

- `templates/CLAUDE.md` → `~/.claude/CLAUDE.md`. The working contract: plan with a challenge, file a record per step, quiet output, ETAs in measured time.
- `templates/settings-statusline.json` → merge into `~/.claude/settings.json`. Live job progress / ETA in the status bar; needs `progress/eta.py` at `~/.claude/skills/progress/` (copy it from `plugins/reflexes/skills/progress/`).

## Known rough edges

- `/progress` and the status bar read `~/.claude/skills/progress/eta.py`; a plugin install lives elsewhere, so copy that folder once (above).
- Some skills mention SEVEL paths (`../AGP`, `docs/lab/profile.md`) in examples; run `/lab:init` in your own repo to create your profile.
- `update-docs` / `lab/reference/gen_docs.py` assume the lab plugin sits at `~/.claude/skills/lab/`.

## Regenerating the guide

```bash
uv run --with reportlab python tools/gen_stack_guide.py
```

Reads each skill's frontmatter; add a French phrase to `tools/phrases_fr.json` when you add a skill (the script refuses to run without it). macOS fonts.
