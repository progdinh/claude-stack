---
name: where
description: Tell the user where something lives on disk — a file, folder, document, PDF, skill, config, log, report, or output that came up in this conversation or that they describe loosely ("the pdf", "the guide", "that decisions file", "where did you put the report"). Answers with the exact path, one line on what it is, and the command to open it; opens it if asked. Use for "/where", "where is X", "what's the path of X", "where did you save that", "open the X".
argument-hint: <the thing> [--open]
effort: low
metadata:
  group: reflex
  phrase: "Where is that file? The exact path, one line on what it is, and how to open it."
---

# where — the path of a thing

**Looking for:** $ARGUMENTS

## Find it — cheapest source first
1. **This conversation.** If I created, edited, read, or mentioned it, I already
   know the path. Use that; don't search.
2. **Known homes:** `~/.claude/skills/` (personal skills), `~/.claude/skills/lab/`
   (plugin: `GUIDE.md`, `README.md`, `SKILLS.md`, the two PDFs, `reference/`),
   `~/.claude/CLAUDE.md`, `~/.claude/settings.json`, `~/.claude/eta-log.jsonl`,
   the project's `docs/`, its lab profile's Paths table, the memory directory.
3. **Search**, only if 1–2 fail: one `find`/glob by name fragment, or one grep
   by a distinctive phrase. Project first, then home. No deep crawls.

## Output — this shape, nothing else

```
<exact/absolute/path>
  <what it is, in a few words> · <modified when, if useful>
  open: <the command — `open <path>` on macOS, or "clickable above">
```

- Several plausible matches → list up to 4, best first, one block each; say
  which I think they mean.
- A folder → the path plus its 3–5 most relevant entries.
- **Verify it exists** before answering (one `ls`/stat) — a path I remember
  may have been moved, renamed, or deleted. If it's gone, say so and where it
  went if I know.
- `--open`, or "open the …" → run the open command too, then just the path.
- Not found → say so in one line, with the closest thing that does exist.
  Never invent a path.

## Rules
- No explanation of the file's contents — that's a different question.
- Paths exact and absolute (or `~`-prefixed), in backticks, so they're clickable.
- Don't derail: answer, stop, resume whatever was in progress.
