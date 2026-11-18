---
name: perf-investigation
description: Investigate a performance problem — latency, throughput, memory, energy, cost — by measurement rather than guesswork: define the metric and budget, reproduce and measure before hypothesising, locate where the time or bytes actually go, change one thing, re-measure, and record before/after. Use for "this is slow", "why is p99 high", "it doesn't fit in memory", "make it faster/cheaper", profiling requests, or before any optimisation work.
argument-hint: <what is slow / too big / too expensive>
metadata:
  group: trust
  phrase: "Slow, too big, too costly: measure first, find where the cost really is, change one thing, re-measure."
---

# Performance investigation

**Problem:** $ARGUMENTS

## Project context (lab profile, injected)

!`cat docs/lab/profile.md 2>/dev/null || cat .claude/lab.md 2>/dev/null || echo "NO LAB PROFILE FOUND. Use defaults under docs/lab/ and generic currencies. Say so in one line; suggest /lab:init."`

Working contract: [contract.md](../../reference/contract.md). The rule that
matters: **no optimisation before a measurement says where the cost is.**
Intuition about hot spots is wrong often enough that acting on it first is
the slow path.

## 1. Define the target — before touching anything
- **Metric**, precisely: which latency (p50/p99/max), of what, measured where;
  which memory (peak working set, RSS, a specific SRAM); per what unit.
- **Budget**, from the profile, with provenance. If there is none, that's the
  first finding — "faster" with no target never finishes.
- **Load / input conditions** that matter (request rate, input size, cold vs
  warm, battery level, concurrent DMA traffic…).
- Tail vs mean: if the outcome depends on the worst case, the mean is a proxy.

## 2. Reproduce and measure the baseline
A command that produces the number, runnable again. n runs, report spread.
Measure **on the real target** if the claim is about the real target; a
laptop number for an MCU, or a dev-box number for production, is labelled an
estimate every time. Save raw output under the artifacts path.

## 3. Find where it goes — top-down, not by suspicion
Break the total into parts that **sum to the total** (a budget table). If the
parts don't add up, the missing piece is the finding. Use the cheapest tool
that answers: timestamps around stages → a sampling profiler → tracing /
hardware counters. Look for fixed overhead (the cost at zero work), queueing
(utilisation near 1 → tail explodes), data movement (copies, cache misses,
bus/PSRAM/PCIe/network crossings, serialisation), and waiting (locks, I/O,
GC, a slower peer).

Classify the bottleneck: **compute-bound / bandwidth-bound / capacity-bound /
latency-bound (round trips) / contention-bound.** Each has different fixes;
optimising the wrong class does nothing.

## 4. Hypothesis, with a predicted number
"X is N% of the total; removing it should take the metric from A to ~B."
A hypothesis without a predicted magnitude can't be wrong, so it can't teach
anything. Check the limiting case: if this part cost zero, would the budget be
met? If not, it isn't the (only) problem.

## 5. Change one thing, re-measure, same conditions
Compare against the prediction. Far off → the model of the system is wrong;
that's more valuable than the speedup. Keep or revert on the number, not on
how clever the change was. Repeat from step 3 — the bottleneck moves.

## 6. Stop when the budget is met
Not when it's as fast as possible. Record what was left on the table.

## 7. Record
`lab:stage-report`: before/after table with conditions and n, the budget
breakdown, what was tried and **didn't** help (with numbers — this is what
stops the same dead end next time), residuals. Choices → `lab:record-decision`.

## Guards
- Never report an improvement without the baseline measured the same way, same day.
- Beware measuring the measurement (profiler overhead, logging in the hot path).
- Correctness check after every change — a fast wrong answer is not a result.
- If the fix is architectural, stop and go to planning mode with `lab:challenge-design`.

End with the four-part TL;DR: before → after against budget, leading.
