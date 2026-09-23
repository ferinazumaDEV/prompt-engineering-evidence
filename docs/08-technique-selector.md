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

## Dated notes

Additive notes that qualify a row of the table above. Each carries its date; the table keeps its original wording.

### 2026-09-23 — reasoning models: reach for the thinking control before the prompt

- On Claude Opus 5.5, "Lowering effort reduces thinking, and with it cost and latency, more reliably than prompt instructions do"; in chat system prompts, Anthropic says to consider removing instructions that tell the model to think carefully before answering (Source: Anthropic, Prompting Claude Opus 5.5, vendor documentation)(https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5).
- On Gemini 3, Google says: "If you were previously using complex prompt engineering (like chain of thought) to force Gemini 2.5 to reason, try Gemini 3 with thinking_level: \"high\"" (Source: Google, Gemini 3 developer guide, vendor documentation)(https://ai.google.dev/gemini-api/docs/gemini-3).
- OpenAI's reasoning page keeps "Avoid chain-of-thought prompts" and names o3, o4-mini and GPT-4.1 as its examples; it does not name GPT-5-class models (Source: OpenAI, Reasoning best practices, vendor documentation)(https://developers.openai.com/api/docs/guides/reasoning-best-practices).
- Few-shot row: vendor guidance diverges. OpenAI says to try prompts without examples first on reasoning models; Google says "always include few-shot examples"; Anthropic says "Include 3–5 examples for best results". The row's grade (`solid` for format conditioning) stands; which vendor's model you run decides the default (Sources: OpenAI, as above; Google, Prompt design strategies)(https://ai.google.dev/gemini-api/docs/prompting-strategies) (Anthropic, Prompting best practices)(https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
- Self-consistency row: the majority vote has a measured failure mode. Sampled trajectories cluster into a few "reasoning basins", and the vote picks the most stable basin rather than the most accurate one, so a correct answer can be present and outvoted; measured on Qwen3-4B and Llama-3.1-8B, not on frontier models (Source: Cai et al. 2026, ARBITER, preprint)(https://arxiv.org/abs/2605.26172).
- Long-input row: the lost-in-the-middle effect is strongest when inputs occupy up to about 50 percent of the context window; beyond that the primacy bias weakens while the recency bias stays relatively stable, which is consistent with "query last" but not with "the middle is always lost" (Source: Veseli et al. 2025, preprint)(https://arxiv.org/abs/2508.07479).

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
