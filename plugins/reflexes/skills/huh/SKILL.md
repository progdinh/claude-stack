---
name: huh
description: Ultra-concise clarification of a term, acronym, symbol, number, or sentence that came up in this conversation — what it means in general and what it meant HERE — in five lines or fewer, without derailing the task in progress. Use when the user asks "what is X", "what does X mean", "huh?", "wait, what's X", "explain that line", or otherwise wants a quick side clarification rather than a full explanation.
argument-hint: <term, phrase, or "that last line">
effort: low
metadata:
  group: reflex
  phrase: "What does that mean? Three lines: the plain definition, what it meant here, a tiny example."
---

# huh — quick clarification

**Clarify:** $ARGUMENTS

This is a side question. Answer it and get out of the way.

## Output — exactly this shape, nothing else

```
**<term>** — <plain-language definition, one sentence, no jargon it doesn't define>.
Here: <what it referred to in THIS conversation — the specific thing, file, number, or step>.
e.g. <one tiny concrete example or the actual number — only if it helps; otherwise omit the line>
```

- **Five lines maximum. Usually three.** No preamble ("Great question"), no
  headers, no bullet lists, no closing offer ("want me to go deeper?"), no
  TL;DR block.
- **"Here:" is the important line.** A dictionary definition is what the user
  could have searched; what they can't search is what *I* meant by it when I
  said it. Point at the exact spot: the message, the file, the table row.
- Plain words. If the definition needs another piece of jargon, swap it for
  the everyday version rather than defining two things.
- Several terms asked at once → one line each, `**term** — definition · here: …`.
- "That last line" / "that" / no argument → clarify the most recent sentence
  of mine that carries the most jargon; quote its first few words so it's
  clear which one.

## Honesty rules

- **If I used the term loosely or wrongly, say so first**, in one line:
  `Correction: I said X; strictly it's Y.` That's worth more than the definition.
- If it's ambiguous, give the reading that fits this conversation, then at
  most one line: `(Could also mean …)`.
- If I don't know, or it was a number I assumed rather than measured, say
  that plainly — don't dress a guess as a definition.
- Made-up-by-me names (a hypothesis label like "H3", a kill test "K1", an
  ansatz "A2") are defined by pointing to where they were introduced.

## Don't derail

- No tools unless the term lives in a file I need to check (then one Read or
  Grep, no more). No web search for a definition I already know.
- Don't change the plan, don't restart the task, don't re-summarise the
  session. After answering, the work in progress continues exactly where it
  was; if I was mid-task, resume it in the same turn without announcing it.
- If the question is actually big (it needs a derivation, a comparison, a
  decision), give the three-line version anyway, then one line naming the
  right tool: `Bigger than a huh — /lab:explore-and-report <x>`.
