# Experiment: the token cost of few-shot prompting

**Question.** Few-shot prompting is everywhere. What does it *cost* — in input
tokens, and therefore in money — to add each example?

**What this measures.** The input size of the same task at 0, 1, 3, and 5 shots,
and the projected spend at scale. Deterministic, offline, no API key, no network.

**What this does not measure.** Whether few-shot makes the *answer* better. That
is an efficacy question; it lives in [`../../../data/techniques.yml`](../../../data/techniques.yml)
(`few-shot-examples`, graded **solid**) with its primary sources. Here we only
price the context, because that cost is real, grows linearly with each example,
and is almost always ignored when people reach for "just add a few examples."

## Run it

```sh
python3 measure.py                       # table
python3 measure.py --json                # machine-readable
python3 measure.py --price-per-1k 0.003 --calls 100000
```

Only the Python standard library is used, so it runs anywhere and returns the
same numbers every time.

## Result (as of 2026-08-27)

```
shots |  chars |  tokens (est.) | x vs 0-shot | USD / 100,000 calls
-------------------------------------------------------------------
    0 |    131 |          29-33 |        1.0x | $9.31
    1 |    187 |          40-47 |       1.39x | $13.01
    3 |    322 |          68-80 |       2.39x | $22.27
    5 |    465 |         95-116 |       3.39x | $31.64

Assumes $0.0030 per 1K input tokens over 100,000 calls. Measures input cost only, not answer quality.
```

Token counts are estimates from two documented heuristics (~4 chars/token and
~4/3 tokens/word); the table shows the band. The **ratio** between variants is
what matters and is stable across tokenizers. Takeaway: five examples roughly
multiplies the input you pay for on **every single call** — worth it when the
examples move quality (see the ledger), wasteful when they don't.
