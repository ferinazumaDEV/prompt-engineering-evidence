# Claims and maturity

This file defines the maturity vocabulary used across the repository, says what counts as a source, and lists every claim the repository makes with its maturity — including the claims that do **not** yet have a row in the evidence ledger. The ledger, [`data/techniques.yml`](data/techniques.yml), remains the machine-readable source of truth for the graded techniques; this page is the human-readable register around it.

## Vocabulary

- **established** — a reproducible effect, at least one primary source with a URL, and a stated scope. In the ledger this value is spelled **`solid`**: `solid` is an alias of `established`, kept so the ledger's CI validator passes unchanged.
- **mixed** — the effect is conditional on scope: it helps under some conditions and not others, and the scope matters more than the technique.
- **experimental** — asserted in this repository without a primary source or an experiment yet. Equivalent to *needs-verification*: the claim stays visible, and so does the gap. Nothing graded `experimental` is a ledger row; a row needs a primary source to exist.
- **folklore** — widely repeated, with no reproducible evidence, or actively debunked. Where a null-result source exists, it is cited.
- **reproducible** — `"yes-offline"` | `"yes-llm"` | `"paper-only"` | `"no"` — always a quoted string, so YAML loaders never turn `no` into a boolean.

## Source vs primary source

- A **source** is where a claim was read: a blog post, a talk, a thread, a guide, this repository.
- A **primary source** is the paper or vendor page that measured or stated the thing itself — an arXiv or DOI link, or the vendor's own documentation URL. Ledger grades rest on primary sources only (see [`CONTRIBUTING.md`](CONTRIBUTING.md)); [`SOURCES.md`](SOURCES.md) lists them.

## Claim register

### Ledger rows

Eight techniques, graded in [`data/techniques.yml`](data/techniques.yml): **3 established** (ledger value `solid`), **2 mixed**, **3 folklore**. Reproducible: **1 yes-offline**, **2 yes-llm**, **2 paper-only**, **3 no**. Each row carries its own primary sources and scope.

| Ledger id | Maturity | Reproducible |
|---|---|---|
| `few-shot-examples` | established (`solid`) | yes-offline |
| `data-before-instruction` | established (`solid`) | paper-only |
| `self-consistency` | established (`solid`) | yes-llm |
| `chain-of-thought` | mixed | yes-llm |
| `positive-over-negative-instructions` | mixed | no |
| `take-a-deep-breath` | folklore | paper-only |
| `temperature-zero-determinism` | folklore | no |
| `threats-and-tips` | folklore | no |

### Claims outside the ledger

These appear in the prose but have no ledger row. A claim with no primary source is `experimental` until one is cited; a claim that already has a primary source carries its real maturity, and only the row is missing.

| Claim | Where | Maturity | Primary source |
|---|---|---|---|
| Grounding (RAG), permission to say "I don't know", and asking for citations reduce fabrication | [`docs/08`](docs/08-technique-selector.md) | experimental | none cited yet |
| Structured output / tool-calling is reliable for output *validity* | [`docs/08`](docs/08-technique-selector.md) | experimental | none cited yet |
| Explaining the *why* of a rule works better than a longer list of "don't" rules | [`docs/08`](docs/08-technique-selector.md) | experimental | none cited yet |
| Running an eval on your own task is the meta-technique | [`docs/08`](docs/08-technique-selector.md) | experimental | none cited yet — a methodological stance, not a measured effect |
| Role/persona prompts shape style but do not improve accuracy on objective tasks | [`FOLKLORE.md`](FOLKLORE.md#role-prompting) | folklore (for accuracy; style effects are real) | Zheng et al. 2024 — [arXiv:2311.10054](https://arxiv.org/abs/2311.10054) |
| Forcing strict JSON output can cost reasoning quality | [`FOLKLORE.md`](FOLKLORE.md#json-reasoning) | mixed | Tam et al. 2024 — [arXiv:2408.02442](https://arxiv.org/abs/2408.02442) |
| XML tags help because they disambiguate structure, not because of a special XML mode | [`FOLKLORE.md`](FOLKLORE.md#xml-magic) | mixed (delimiters help; XML-specific magic is folklore) | Anthropic, [Structure prompts with XML tags](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#structure-prompts-with-xml-tags) — vendor documentation; no independent measurement |
| Prompt-level defences against prompt injection are not a control you can rely on | [`docs/05`](docs/05-security.md) | folklore | Greshake et al. 2023 — [arXiv:2302.12173](https://arxiv.org/abs/2302.12173); [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), LLM01 |

The three `FOLKLORE.md` claims have primary sources but no ledger row; adding rows changes the archived counts and is a maintainer decision. Until then they are not counted in the ledger totals above or in `about.jsonld`.

## Per-technique format

A new technique entry in `docs/` follows this order, so a reader (or a crawler) always finds the same six things in the same place:

1. **Definition** — what the technique is, in one or two sentences.
2. **Answer** — does it work, and the maturity from the vocabulary above.
3. **Evidence** — what was measured, on which models, when; a number carries its limitation in the same sentence.
4. **Implementation** — how to apply it.
5. **Limitations** — the scope: where it does not apply.
6. **Sources** — primary sources first, then the sources where the claim was read, labelled as such.

---

Licensed **CC BY-SA 4.0**, like the rest of the prose ([`LICENSE`](LICENSE)).
