# 08 · Technique selector — which technique for which problem

**Start from your problem, not from a technique.** Most prompt failures are the wrong tool applied confidently. This page maps a symptom to the technique the evidence supports — and, just as often, to *"you don't need a technique, you need an eval / a schema / a different model."*

| Your problem | Reach for | Evidence | Not this |
|---|---|---|---|
| Multi-step math/logic is wrong | Chain-of-thought (ask for step-by-step) | `mixed` (helps on reasoning tasks; redundant on reasoning models) | CoT on lookup/knowledge tasks — no gain |
| High-stakes reasoning, cost OK | Self-consistency (sample N, majority vote) | `solid` | Using it on open-ended generation |
| Output format is inconsistent | Few-shot examples + explicit schema | `solid` | Adding examples when a plain instruction already works (wastes tokens) |
| Model ignores part of a long input | Put data first, query last; shorten/chunk | `solid` (lost-in-the-middle) | Trusting the middle of a huge context |
| JSON comes back broken | Structured output / tool-calling + a reasoning field first | `solid` for validity; `mixed` for reasoning cost | Forcing strict JSON *and* expecting full reasoning quality |
| It makes things up | Grounding (RAG), "say 'I don't know'", ask for citations | `solid` (grounding) | Believing a confident answer without a source |
| Behavior breaks on edge cases | Explain the *why* of the rule; add scope | `mixed` | A longer list of "don't" rules |
| Reads untrusted content + has secrets/tools | **Architecture, not a prompt** — break the lethal trifecta | see [security](05-security.md) | "Ignore injections below" in the system prompt (folklore) |
| "Is this technique worth it?" | Run an eval on YOUR task | `solid` (the meta-technique) | Copying a benchmark number from a blog |

## The one rule under all of this

There is no ranking of techniques independent of a task. **The technique is a hypothesis; the eval is the test.** If you can't measure whether a change helped on your own data, you're not doing prompt engineering — you're guessing. See the ledger for what each technique is graded and why: [`data/techniques.yml`](../data/techniques.yml).

---
<!-- ecosystem:start -->
Part of the **ferinazumaDEV** ecosystem. Flagship: **[The GEO Handbook](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook)**. Hub: **[zentimes.es](https://zentimes.es)**. By **[ferinazumaDEV](https://github.com/ferinazumaDEV)**.
<!-- ecosystem:end -->
