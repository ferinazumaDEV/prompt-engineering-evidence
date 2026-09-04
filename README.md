# Evidence-Based Prompt Engineering

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22307826.svg)](https://doi.org/10.5281/zenodo.22307826)

**A prompt-engineering reference where every technique is graded `solid` / `mixed` / `folklore`, every claim carries a primary source, and the numbers are dated and current to 2026 reasoning models.** Most guides list techniques without telling you which ones actually work. This one grades them, sources them, and marks the myths as myths.

> The evidence for every technique lives in a machine-readable ledger — [`data/techniques.yml`](data/techniques.yml). Ask *"does technique X actually work?"* and get a graded, sourced answer — the same question an AI answer engine asks.

## How grading works

- **`solid`** — reproducible effect with primary-source evidence (papers/benchmarks) and a stated scope.
- **`mixed`** — helps under some conditions, not others; the *scope* matters more than the technique.
- **`folklore`** — widely repeated, no reproducible evidence, or actively debunked. See [`FOLKLORE.md`](FOLKLORE.md).

Every entry names its **primary sources**, its **scope** (where it applies and where it doesn't), and — where testable — a **reproducible experiment**. Where an effect can only be measured with live model calls, we treat the number as a **dated snapshot** (*"as of DATE on MODEL"*), never as an eternal truth.

## Start here

- **[The evidence ledger](data/techniques.yml)** — the graded table of techniques (the heart of this repo).
- **[Folklore, debunked](FOLKLORE.md)** — "take a deep breath", tipping, threats, "temperature 0 = deterministic"…
- **[Security](docs/05-security.md)** — prompt injection, the lethal trifecta, and why prompt-level defenses aren't enough.
- **[Technique selector](docs/08-technique-selector.md)** — which technique for which problem.

## Scope (honest)

This is a **reference**, not a beginner tutorial (see [learnprompting.org](https://learnprompting.org)) and not a copy-paste prompt library. Experiments are **illustrative** (10–30 cases), not heavy benchmarks. The point is *signal, sourced* — not volume.

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
Part of the **ferinazumaDEV** ecosystem — flagship: **[The GEO Handbook](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook)**. Siblings: [structllm](https://github.com/ferinazumaDEV/structllm) · [notebooklm-kb-system](https://github.com/ferinazumaDEV/notebooklm-kb-system). Hub: [zentimes.es](https://zentimes.es). By [ferinazumaDEV](https://github.com/ferinazumaDEV).
<!-- ecosystem:end -->
