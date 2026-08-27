# Experiments

Reproducible checks that back the ledger's grades. Tiered by **durability**, because honesty about reproducibility is the whole point of this repo.

## `offline/` — deterministic, no API key, doesn't rot

Lead with these. They run on recorded fixtures or pure computation (token counts, schema validity, injection landing rates, example-order effects on saved outputs). Same input → same result, forever. These are what "reproducible" should mean.

## `llm-measured/` — dated snapshots

Some effects can only be measured with live model calls. Those are **not eternal**: they cost money, are non-deterministic, and change when the model updates. Every result here is stamped `as of DATE on MODEL-vX, N=…, seed=…`. Treat them as evidence *on that date*, not as constants. A `weekly-update` job re-runs them and flags numbers that have drifted.

## Status

Experiments are published on the weekly cadence (see [`../updates/`](../updates/)). The ledger grades stand on the primary sources in [`../SOURCES.md`](../SOURCES.md); experiments add local, runnable confirmation as they land. **We would rather ship no experiment than a misleading one** — that is the same discipline the ledger enforces.
