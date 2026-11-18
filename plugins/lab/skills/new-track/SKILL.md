---
name: new-track
description: Open a new research track (sub-project) inside a multi-track project — a folder named by the user, a CLAUDE.md stating the ONE question it answers and what it is not, a decisions log, a roadmap, an explorations index, a row in the root project table — and offer to move in records that were misfiled in a neighbouring track, with dated cross-links. Use when a question belongs to no existing track, or when explore-and-report / record-decision flagged "no matching track".
disable-model-invocation: true
argument-hint: <folder-name> "<the one question this track answers>"
metadata:
  group: start
  phrase: "Open a new research track: its one question, what it is not, empty records, root table row; moves in misfiled records."
---

# Open a new track

**Arguments:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND — infer the track convention from the existing sub-project folders and the root CLAUDE.md table."`

Working contract: [contract.md](../../reference/contract.md).
`init` configures the process for the whole project, once. `run` takes one
question through the pipeline. This opens **one track** — rarely.

## 0. Two gates — refuse politely if either fails

- **The question.** One sentence, ending in a question mark, that the track
  exists to answer. No question → no track: a folder without one is a junk
  drawer. If the argument gives only a name, ask for the question (one line)
  and stop.
- **It really has no home.** Read the root project table and each existing
  track's stated question. If an existing track's question covers it, say
  which and stop. "Nearest neighbour" is not "covers it": a track that merely
  *consumes* this work's output is a neighbour, not a home.

## 1. The name is the user's

Use the folder name given. If none was given, propose **one** and ask — do not
create first and rename later. You may say, in one line, if the name collides
with an existing folder, repo, or acronym in the project (check the root table
and sibling directories) — then do what the user says. Naming is branding and
scope; it is not yours to optimise.

## 2. Create — only this, nothing speculative

Match the neighbouring tracks' formats; read one of them first.

| File | Contents |
|---|---|
| `<track>/CLAUDE.md` | pointer to the root contract · **the question** · **what this track is not** (each non-goal names the track that *does* own it) · its currencies with units · where its records live. Any naming or acronym rule goes at the top. Under ~50 lines. |
| `<track>/docs/decisions.md` | the house header · first entry **"This track exists"** — Decision / Why / **Falsifier** (default: "still one record in ~a month → premature; a root-level note would have done") · `## Open / not yet decided` at the bottom |
| `<track>/docs/roadmap.md` | the stage table header + only stages that are real now: what is done (moved-in records), what is proposed with a price, what is blocked and on what |
| `<track>/explorations/README.md` | index table header (`Date \| Topic \| Source \| Status`) + a "Still to file" table |

Not created: `derivations/` (made by `derive-ansatz` on first use), code,
manifests, `artifacts/`. Then add **one row to the root project table**
(path · question · status) and, if a lab profile exists, the track's paths to
its Paths table.

## 3. Offer to move in misfiled records — list first, never silently

Grep the neighbouring tracks for the topic. Present what you would move and
what you would leave, then move on a yes. Rules, all learned the hard way:

- **Split by what the old track consumes.** The half it uses as an input
  stays there (with a pointer); the rest moves. A record that is genuinely
  about the old track's question stays whole.
- **Untracked files: `mv`. Tracked: `git mv`.** Check `git status` first.
- **Fix the relative links inside every moved file**, and add a dated line:
  *"Filed <date> under <old path>; moved here <date> when this track opened."*
- **Old index:** remove the row, leave a one-line dated pointer to the new
  path. **Old decisions log:** replace a moved entry with a dated pointer;
  the moved text is carried over **unchanged**, labelled with both dates.
  Never rewrite history on the way.
- **Then grep the whole project for the old path** and update every
  reference. Finish with a grep that returns zero stale hits — say the count.

## 4. Close

No commit. No code. Update the project memory / profile with the track's
existence and any naming rule. One closing line: folder, files created,
records moved (count), stale references remaining (must be 0), and the
suggested first skill to run in the new track.
