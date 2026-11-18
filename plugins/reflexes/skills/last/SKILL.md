---
name: last
description: Concise, readable summary of what just happened IN THIS CONVERSATION — what was asked, what Claude actually did, the result, which files changed, and what was left undone — as six short labelled blocks. Use when the user asks "what did you just do", "summarise the last step", "what happened", "what changed", "recap that", or wants a quick digest of the previous turn(s) rather than a project-wide status. Source is the chat, not the repo's docs or git history.
argument-hint: [N turns | session | <topic>]
effort: low
metadata:
  group: reflex
  phrase: "What just happened in this chat? Six short blocks: asked, did, result, files changed, left open, next."
---

# last — what just happened

**Scope:** $ARGUMENTS

Summarise **this conversation**, not the project. (`/lab:tldr` is the other
one: project state, read from files. This reads the chat.)

## Scope
| Argument | Covers |
|---|---|
| *(none)* | everything since the user's previous message — the last step |
| a number `N` | the last N exchanges |
| `session` | the whole conversation, grouped by step |
| a topic | only the parts of the conversation about that topic |

## Output — this shape, rendered as markdown (NOT inside a code block)

**Correction** *(only if something said earlier was retracted — always first)*
- what I said → what is actually true, with the number

**Asked**
- what the user wanted, in their terms

**Did**
- one bullet per distinct action: verb + object

**Result**
- the outcome, **numbers in bold**, one fact per bullet

**Changed**
- one path per bullet (group a folder as `dir/*.json (25 new)`); commit hash if any

**Open**
- one bullet per thing not done, failed, skipped, unmeasured, or untested

**Next**
- the single most useful next action

### Readability rules — these are why the format exists

- **Label alone on its line, in bold. Content underneath as bullets. A blank
  line between blocks.** Never put label and content on one line; never
  produce a paragraph.
- **One fact per bullet, and each bullet fits on one terminal line**
  (~90 characters). A bullet that needs a second clause is two bullets. If a
  block would need more than **4 bullets**, keep the 4 that matter most and
  end with `- (+N more)` rather than cramming.
- Cut connective prose ("then", "so that", "which meant"). Bullets are
  fragments, not sentences.
- Bold only numbers and the one word that carries a bullet. Paths in
  backticks, exact.
- No preamble, no closing offer, no TL;DR block on top of it.
- Drop a block only if it would be literally empty (`Changed` for a pure
  question) — except **Open**, which always appears; if genuinely nothing is
  open, one bullet saying why ("verified by running it").

### Content rules

- **`Did` is what happened, not what was intended.** Planned five, did three →
  say three; the other two go under `Open`.
- **Distinguish verified from unverified** in `Result`: "ran, passed" vs
  "written, not run". An untested thing is never reported as working.
- Numbers carry units and, where it matters, provenance (measured / assumed).
- Plain words — if a term needs explaining, that's a `/huh`.

## Rules

- **Source is this conversation.** Don't read docs, don't run `git log`, don't
  re-open files to reconstruct what happened. One exception: if unsure whether
  an edit actually landed, one quick check is fine.
- **If there is no conversation to summarise** (fresh session): say so in one
  line, then offer `/lab:tldr` for project state, or the last commit +
  uncommitted changes — and if the user evidently wants the latter, give it,
  **labelled as coming from git, not from the chat**.
- Don't continue the work, don't change the plan, don't re-summarise older
  steps unless asked. Answer and stop; if I was mid-task, resume it in the
  same turn.
- Don't pad a small step. Three one-bullet blocks is a complete answer.
