---
name: workshop-build
description: Design a hands-on workshop — a timed run-of-show where every participant has a working artefact on their own machine well before the end, with setup that can't fail in the room, a deliberate failure to debug, checkpoints, and a take-home extension.
disable-model-invocation: true
argument-hint: "<topic>" [--minutes 60] [--level beginner|intermediate|advanced] [--format tool|field] [--audience "<who>"] [--hardware "<kit>"] [--out <dir>]
metadata:
  group: organise
  phrase: "A timed hands-on workshop: working artefact by two-thirds time, setup that cannot fail in the room, one planned failure to debug."
---

# Build a workshop

**Arguments:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Fine for this skill — infer audience and format from the arguments."`

## Flags
| Flag | Meaning | Default |
|---|---|---|
| `--minutes` | total length | 60 |
| `--level` | audience level | beginner |
| `--format` | **tool** = "one hour, one tool, hands on the keyboard"; **field** = "one hour, one field, from the ground up" | tool |
| `--audience` | who is in the room | students, mixed background |
| `--hardware` | physical kit involved, if any | none |
| `--out` | where to write materials | `workshops/<slug>/` |

## Design rules — these are the point of the skill

1. **One sentence of promise.** "In 60 minutes you will have X running on your
   laptop." If it needs "and", it's two workshops.
2. **Working artefact by two-thirds time** (minute 40 of 60). Everything after
   is extension, not rescue. Design backwards from that moment.
3. **Keyboard within 5 minutes.** No slides-first. Theory arrives *after* the
   thing it explains has been seen working (or failing).
4. **Setup cannot be allowed to fail in the room.** One command, tested on a
   clean machine on each OS in the audience; a pre-workshop check script; a
   zero-install fallback (hosted notebook / container / pre-flashed board);
   offline copies of anything downloaded. Budget: nobody spends more than
   5 minutes on setup.
5. **A failure on purpose.** One planned step where it breaks in an
   instructive way, and the room debugs it together. This is what people
   remember, and it's what separates having typed from having understood.
6. **Checkpoints with checkable state.** Every ~10 minutes: "you should now
   see ___". A `checkpoint-N` branch or folder so anyone lost can jump forward
   instead of dropping out.
7. **Three speeds.** A core path everyone finishes, a stretch for the fast, a
   catch-up for the slow (`lab:exercise-ladder` builds these).
8. **Ends with a door, not a wall.** One concrete next thing to build alone,
   and where to get help.

## Procedure

1. Pin the promise, the audience's assumed knowledge (list it — then halve
   it), and the artefact.
2. Build the artefact yourself first, end to end, timing it. Multiply your
   time by **3–4** for a room of beginners. Cut scope until it fits — cutting
   is the main design act.
3. Write the run-of-show: minute · what the room does · what the lead says
   (one line) · checkpoint state · likely failure + fix.
4. Write the materials into `--out`: `README.md` (promise, prerequisites,
   setup, check script), the starter code, `checkpoint-N/`, `solutions/`,
   `LEAD_NOTES.md` (run-of-show, the planned failure, known pitfalls per OS,
   what to cut if running late), `NEXT.md`.
5. **Run the setup and every checkpoint from scratch** in a clean directory
   and report what actually happened. Untested materials are labelled
   untested.
6. With `--hardware`: per-seat kit list, spares count (assume 10–15%
   failure), power and safety notes (LiPo, soldering, moving parts), and a
   no-hardware path for whoever's board is dead.

## Guards
- If recorded or published: no secrets in materials, licences checked for
  every asset and dataset, API keys via per-participant caps or a mock.
- Don't teach the tool's whole surface. Teach the one path to the artefact.
- A workshop that only works on the lead's laptop is not finished.

End with: the promise, the minute-40 artefact, the planned failure, what was
actually tested, and what is still untested.
