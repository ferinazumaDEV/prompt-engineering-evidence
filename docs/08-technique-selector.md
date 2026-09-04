# 08 · Technique selector — which technique for which problem

**Start from your problem, not from a technique.** Most prompt failures are the wrong tool applied confidently. This page maps a symptom to the technique the evidence supports — and, just as often, to *"you don't need a technique, you need an eval / a schema / a different model."*

| Your problem | Reach for | Evidence | Not this |
|---|---|---|---|
| Multi-step math/logic is wrong | Chain-of-thought (ask for step-by-step) | `mixed` (helps on reasoning tasks; redundant on reasoning models) | CoT on lookup/knowledge tasks — no gain |
| High-stakes reasoning, cost OK | Self-consistency (sample N, majority vote) | `solid` | Using it on open-ended generation |
| Output format is inconsistent | Few-shot examples + explicit schema | `solid` | Adding examples when a plain instruction already works (wastes tokens) |
| Model ignores part of a long input | Put data first, query last; shorten/chunk | `solid` (lost-in-the-middle) | Trusting the middle of a huge context |
| JSON comes back broken | Structured output / tool-calling + a reasoning field first | `experimental` — not yet in the ledger (see [CLAIMS.md](../CLAIMS.md)) | Forcing strict JSON *and* expecting full reasoning quality |
| It makes things up | Grounding (RAG), "say 'I don't know'", ask for citations | `experimental` — not yet in the ledger (see [CLAIMS.md](../CLAIMS.md)) | Believing a confident answer without a source |
| Behavior breaks on edge cases | Explain the *why* of the rule; add scope | `experimental` — not yet in the ledger (see [CLAIMS.md](../CLAIMS.md)) | A longer list of "don't" rules |
| Reads untrusted content + has secrets/tools | **Architecture, not a prompt** — break the lethal trifecta | see [security](05-security.md) | "Ignore injections below" in the system prompt (folklore) |
| "Is this technique worth it?" | Run an eval on YOUR task | `experimental` — not yet in the ledger (see [CLAIMS.md](../CLAIMS.md)) | Copying a benchmark number from a blog |

## The one rule under all of this

There is no ranking of techniques independent of a task. **The technique is a hypothesis; the eval is the test.** If you can't measure whether a change helped on your own data, you're not doing prompt engineering — you're guessing. See the ledger for what each technique is graded and why: [`data/techniques.yml`](../data/techniques.yml).

---
<!-- ecosystem:start -->
Part of a cluster of open work on making content legible to machines, by **Fernando Aporta Franco** ([ferinazumaDEV](https://github.com/ferinazumaDEV)):

**Three layers on GEO (Generative Engine Optimization)**
- **[The GEO Handbook](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook)** — the reference: what to do and why, with sources (theory).
- **[The GEO Cookbook](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook)** — six reproducible before/after recipes with offline measurements (practice).
- **[Evidence-Based Prompt Engineering](https://github.com/ferinazumaDEV/prompt-engineering-evidence)** — a graded, sourced ledger of prompting techniques (the input side).

**Small open tools**
- [typedout](https://github.com/ferinazumaDEV/typedout) — reliable structured output from OpenAI and Anthropic, with a provider interface for others.
- [politeclient](https://github.com/ferinazumaDEV/politeclient) — a polite HTTP client for Python: retries with backoff, per-host rate limiting, caching, pagination.
- [webhook-replay](https://github.com/ferinazumaDEV/webhook-replay) — capture a webhook once, then replay it at your local app as many times as you need.
- [scaffld](https://github.com/ferinazumaDEV/scaffld) — scaffold fully-wired Python projects from templates, with a TUI.
- [framesig](https://github.com/ferinazumaDEV/framesig) — find on-screen events in video by pixel signature; no ML.
- [notebooklm-kb-system](https://github.com/ferinazumaDEV/notebooklm-kb-system) — a token-efficient second brain for AI agents on top of NotebookLM.

Hub and writing: **[zentimes.es](https://zentimes.es)**.
<!-- ecosystem:end -->
