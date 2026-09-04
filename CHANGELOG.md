# Changelog

All notable changes to **Evidence-Based Prompt Engineering** are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Because this
is an evidence ledger rather than software, a "version" is a state of the corpus: which
techniques are graded, on what sources, and with which numbers.

Numbers measured against a live model are dated snapshots tied to a named model. They are
not corrected in place when a model changes — a new entry is added, and the old one keeps
its date.

> Version headings are plain text on purpose: a changelog cannot link its own tag before
> that tag exists without failing the link check. Compare views are one click from the
> [releases page](https://github.com/ferinazumaDEV/prompt-engineering-evidence/releases).

## [Unreleased]

### Added

- **DOI.** `v0.1.0` is archived on Zenodo, so the ledger is citable by a persistent
  identifier instead of a repository URL. The concept DOI
  [`10.5281/zenodo.22307826`](https://doi.org/10.5281/zenodo.22307826) always resolves to the latest release. Recorded in the
  README badge and citation, `CITATION.cff`, `about.jsonld` and `llms.txt`.

## [0.1.0] — 2026-09-04

First tagged state of the corpus.

### Added

- **The evidence ledger** — [`data/techniques.yml`](data/techniques.yml), eight graded
  techniques: three `solid`, two `mixed`, three `folklore`. Each entry names its primary
  sources and the scope in which it applies.
- **[`FOLKLORE.md`](FOLKLORE.md)** — widely repeated advice with no reproducible evidence,
  or actively debunked, stated as such rather than omitted.
- **[`SOURCES.md`](SOURCES.md)** — the primary sources behind the gradings.
- **One reproducible offline experiment** — [`experiments/offline/token-cost`](experiments/offline/token-cost/),
  which runs without network or API key.
- Two reference chapters: [security](docs/05-security.md) (prompt injection, the lethal
  trifecta, and why prompt-level defences are not enough) and a
  [technique selector](docs/08-technique-selector.md).
- [`templates/technique-entry.template.yml`](templates/technique-entry.template.yml) so a
  contributed entry carries grade, scope and sources by construction.
- `CONTRIBUTING.md` with the "cite or do not grade" rule, `llms.txt`, `about.jsonld`,
  and licences GitHub can detect: CC BY-SA 4.0 for the prose, MIT for the code.

### Scope of the claims

Eight graded techniques is a **starting corpus, not a survey**. Experiments here are
illustrative (10-30 cases), not benchmarks, and the README says so. A `solid` grade means
a reproducible effect with a primary source and a stated scope — it does not mean the
technique helps in every setting, which is exactly what the `scope` field is for.
