# sevel-stack — Joseph's Claude Code stack

Two plugins plus two drop-in templates, as used at the hackathon.

## Quick start (do this first)

The reflexes are meant to be typed as one word: `/go`, `/huh`, `/last`, `/progress`, `/your-take`. A plugin adds a prefix (`/reflexes:go`), so copy the skills once and drop it:

```bash
git clone https://github.com/progdinh/claude-stack && cd claude-stack
tools/install-bare.sh        # adds the reflex skills to ~/.claude/skills, never overwrites
```

Then install the `lab` plugin below (its commands keep the `/lab:` prefix on purpose: that is the research process). This also puts `progress/eta.py` where `/progress` and the status bar expect it.

## Install

```
/plugin marketplace add progdinh/claude-stack     # or a local path
/plugin install lab@sevel-stack
```

Prefer prefixes over copying? `/plugin install reflexes@sevel-stack` gives `/reflexes:go`, `/reflexes:huh`, … instead. Don't do both.

| Plugin | What you get |
|---|---|
| `lab` | `/lab:run`, `derive-ansatz`, `draft-ideas`, `challenge-design`, `explore-and-report`, `record-decision`, `stage-report`, `tldr`, `prototype`, `novelty-claim`, `init`, … — a research process where every step leaves a filed, falsifiable, priced record. Guide: `plugins/lab/GUIDE.md`. |
| `reflexes` | `/reflexes:go`, `huh`, `last`, `progress`, `rectify`, `update-context`, `big-job`, `where`, `your-take`. Short skills that read the conversation and answer briefly. |

**Guide (3 pages per language):** [English](docs/stack-guide.en.pdf) · [Français](docs/stack-guide.fr.pdf). The nine skills I use most come first.

## Templates (not installable as plugins)

- `templates/CLAUDE.md` → `~/.claude/CLAUDE.md`. The working contract: plan with a challenge, file a record per step, quiet output, ETAs in measured time.
- `templates/settings-statusline.json` → merge into `~/.claude/settings.json`. Live job progress / ETA in the status bar; needs `progress/eta.py` at `~/.claude/skills/progress/` (copy it from `plugins/reflexes/skills/progress/`).

## Known rough edges

- The skills read a per-project profile at `docs/lab/profile.md`. Without one they fall back to generic defaults and say so; run `/lab:init` once per project to create it.

## Regenerating the guide

```bash
uv run --with reportlab python tools/gen_stack_guide.py
```

Reads each skill's frontmatter; add a French phrase to `tools/phrases_fr.json` when you add a skill (the script refuses to run without it). macOS fonts.

## License

MIT, see [LICENSE](LICENSE).
