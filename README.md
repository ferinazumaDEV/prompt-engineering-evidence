# Evidence-Based Prompt Engineering

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22307826.svg)](https://doi.org/10.5281/zenodo.22307826)

## GEO ID Card

| Field | Value |
|---|---|
| **What** | Dataset — Evidence-Based Prompt Engineering |
| **Who** | Fernando Aporta Franco (ferinazumaDEV) — https://github.com/ferinazumaDEV · https://zentimes.es |
| **Claims** | A prompt-engineering reference in which every technique is graded solid, mixed or folklore, and every claim names a primary source. The evidence lives in a machine-readable ledger. This first release grades eight techniques (three solid, two mixed, three folklore) and ships one offline reproducible experiment; it is a sourced starting corpus, not an exhaustive survey. Effects that can only be measured with live model calls are recorded as dated snapshots against a named model, never as standing truths. |
| **Based on** | https://github.com/ferinazumaDEV/generative-engine-optimization-handbook |
| **Sources** | [`SOURCES.md`](SOURCES.md) |
| **Cite** | [`CITATION.cff`](CITATION.cff) · DOI [10.5281/zenodo.22307826](https://doi.org/10.5281/zenodo.22307826) |
| **Canonical** | https://github.com/ferinazumaDEV/prompt-engineering-evidence |
| **Updated** | 2026-09-04 |
| **Version** | 0.1.0 (Release v0.1.0) |
| **Maturity** | mixed overall — 3 established (ledger alias `solid`) · 2 mixed · 3 folklore; reproducible: partial — 1 yes-offline · 2 yes-llm · 2 paper-only · 3 no. See [`CLAIMS.md`](CLAIMS.md). |
| **License** | CC BY-SA 4.0 prose · CC BY 4.0 data/templates · MIT code |

**A prompt-engineering reference where every technique is graded `solid` / `mixed` / `folklore`, every claim carries a primary source, and the numbers are dated and current to 2026 reasoning models.** Most guides list techniques without telling you which ones actually work. This one grades them, sources them, and marks the myths as myths.

> The evidence for every technique lives in a machine-readable ledger — [`data/techniques.yml`](data/techniques.yml). Ask *"does technique X actually work?"* and get a graded, sourced answer — the same question an AI answer engine asks.

## How grading works

- **`solid`** — reproducible effect with primary-source evidence (papers/benchmarks) and a stated scope.
- **`mixed`** — helps under some conditions, not others; the *scope* matters more than the technique.
- **`folklore`** — widely repeated, no reproducible evidence, or actively debunked. See [`FOLKLORE.md`](FOLKLORE.md).

`solid` is the ledger's alias for `established` — see [`CLAIMS.md`](CLAIMS.md) for the full vocabulary (including `experimental`) and the register of claims that have no ledger row yet.

Every entry names its **primary sources**, its **scope** (where it applies and where it doesn't), and — where testable — a **reproducible experiment**. Where an effect can only be measured with live model calls, we treat the number as a **dated snapshot** (*"as of DATE on MODEL"*), never as an eternal truth.

## Start here

- **[The evidence ledger](data/techniques.yml)** — the graded table of techniques (the heart of this repo).
- **[Folklore, debunked](FOLKLORE.md)** — "take a deep breath", tipping, threats, "temperature 0 = deterministic"…
- **[Security](docs/05-security.md)** — prompt injection, the lethal trifecta, and why prompt-level defenses aren't enough.
- **[Technique selector](docs/08-technique-selector.md)** — which technique for which problem.

## Scope (honest)

This is a **reference**, not a beginner tutorial (see [learnprompting.org](https://learnprompting.org)) and not a copy-paste prompt library. One experiment ships today — the offline [token-cost measurement](experiments/offline/token-cost/) for few-shot examples — and future experiments will be **illustrative** (10–30 cases), not heavy benchmarks. The point is *signal, sourced* — not volume.

## How this relates to GEO

[GEO (Generative Engine Optimization)](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook) is about making *content* legible so machines **cite** it (the output side). Prompt engineering is about making *instructions* so machines **execute** them well (the input side). Two sides of one discipline: making content and systems legible to machines.

## How to cite

Every tagged release is archived on Zenodo with a DOI. Cite the **concept DOI** — it always resolves to the latest release. Each release also carries its own version DOI, on its own record page, if you need to pin one exact state of the ledger.

> Aporta Franco, F. (2026). *Evidence-Based Prompt Engineering* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22307826

The same metadata lives in [`CITATION.cff`](CITATION.cff), which GitHub renders as the **"Cite this repository"** button (APA and BibTeX) in the sidebar.

## License

Prose is **CC BY-SA 4.0** ([`LICENSE`](LICENSE)); the ledger (`data/`) and templates are **CC BY 4.0**; code (`experiments/`, scripts, `.github/`) is **MIT** ([`LICENSES/MIT.txt`](LICENSES/MIT.txt)). In short: build on the code freely, credit the words.

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
