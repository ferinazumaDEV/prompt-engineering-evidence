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

Dated 2026-09-23. No grade changed. No ledger row was added: the counts archived with 0.1.2 stand, and
the two candidates for a row are recorded in `CLAIMS.md` and the weekly log instead.

### Added

- `updates/2026-W39.md` — the first weekly log the `updates/` cadence promised; it also records that
  weeks W35–W38 were never logged.
- `FOLKLORE.md` — a tone/politeness entry (`#politeness`, verdict `mixed`) on four 2025–2026 preprints,
  plus dated updates under role prompting (two new primary sources) and temperature zero (Google's
  Gemini 3 guidance to keep temperature at 1.0).
- `CLAIMS.md` — the tone/politeness claim in the register of claims outside the ledger; two more sources
  on the role-prompting claim.
- `SOURCES.md` — a Google block under vendor documentation, a *Tone and politeness* section, and
  Prompting Science Reports 1, 4 and 5, Xiao et al. 2026, Veseli et al. 2025 and Cai et al. 2026 (ARBITER).
- `docs/05-security.md` and `docs/08-technique-selector.md` — a *Dated notes* section each: measured
  injection susceptibility of 2025–2026 graders; thinking controls before chain-of-thought prompting on
  reasoning models; vendor divergence on few-shot; a majority-vote failure mode; positional bias at high
  context utilisation.
- `RELEASING.md` — the Software Heritage visit date as the check that an archive request worked.

### Changed

- `data/techniques.yml` — `last_verified` moved to 2026-09-23 on `chain-of-thought`, `few-shot-examples`,
  `data-before-instruction`, `self-consistency` and `positive-over-negative-instructions`, each after every
  primary source of the row was re-opened; dated `when_not` bullets and new primary sources on those rows
  (Anthropic Opus 5.5 guide, Google Gemini docs, Veseli et al. 2025, Cai et al. 2026, the Internet Archive
  copy of the OpenAI help-center article). `temperature-zero-determinism` gains Google's Gemini 3 source
  but keeps its date: the Anthropic Messages API sentence could not be re-read from the fetched page.
- README *Updated* row (both languages) and `about.jsonld` `dateModified` moved to 2026-09-23.

## [0.1.2] — 2026-09-13

The archived copy had fallen behind again: seven commits landed after `v0.1.1`,
none of them a change to what the ledger says, all of them changes to how a
reader can trust it.

### Added

- **`scripts/validate-ledger.py`, run by CI on every push and pull request
  (`ledger-validate.yml`).** Every ledger entry must have a unique id, at least
  one source that resolves to an arXiv id, a DOI or a URL, no date in the future,
  a `see` target that exists, a `reproducible` value from the documented
  vocabulary, and — for every `yes-*` entry — an `evidence_target` saying what
  the reproduction measures (quality or cost). The three experiments carry it:
  chain-of-thought and self-consistency target quality, few-shot targets cost.
  A ledger that CI cannot validate is a ledger nobody has read closely.
- **`README.es.md`** — a Spanish edition of the README, with a language selector
  at the top of both, and a check (`translations.yml`) that fails when the
  English README changes and the Spanish one is not re-anchored to it. The
  anchor is the content hash of the English file, so it survives squash merges.

### Changed

- The link check gives slow hosts 30 seconds and retries with a pause instead
  of ignoring them: the Zenodo DOI is the most load-bearing link in a repository
  whose point is citability, and a check that has quietly stopped looking at it
  is worse than a slow one.

## [0.1.1] — 2026-09-06

The archived copy had fallen behind. `v0.1.0` was tagged on 4 September and six
commits landed after it, including the CC BY 4.0 licence text the README had
been promising but not shipping, the complete `about.jsonld`, `CLAIMS.md`, and
the sourcing of every ledger claim. A reader who took the archived deposit got a
README pointing at a licence file that was not in it.

### Added

- **[`CLAIMS.md`](CLAIMS.md)** — the maturity vocabulary (`established` / `mixed` /
  `experimental` / `folklore` + `reproducible`), with the ledger's `solid` as an alias of
  `established`, and a register of every claim the prose makes without a ledger row.
- **GEO ID Card** in the README, and the fields `about.jsonld` was missing as the source of
  truth: abstract, version, dates, citation list, maturity counts. `llms.txt` now names the
  version, date, licences, changelog and both sibling GEO repos.
- **Sources.** Meincke et al. 2025 (Prompting Science Reports 2 and 3), Bsharat et al. 2023,
  Debenedetti et al. 2025 (CaMeL), He and Thinking Machines Lab 2025, the Anthropic and OpenAI
  pages behind the vendor claims, and Simon Willison's three primary posts. Five ledger rows
  that pointed at unlinked strings now point at these; no grade changed.

### Changed

- `reproducible: no` is quoted in the ledger so YAML loaders keep it a string.
- Figures carry their limitation in the sentence (Anthropic's 30 percent, Lu et al.'s order effect).
- `docs/08` no longer grades techniques that have no ledger row; those cells read `experimental`.
- The contribution template uses the ledger's schema and passes the validator.
- Ecosystem footers and `ECOSYSTEM.md` carry the cluster's canonical block.
- `experiments/README.md` marks the `llm-measured/` tier as planned; no re-run job ships yet.

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
