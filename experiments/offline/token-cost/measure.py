#!/usr/bin/env python3
"""
token-cost — how many tokens each few-shot example adds to a prompt, and what
that costs at scale.

WHAT THIS MEASURES: the *input* cost of few-shot prompting. Deterministic,
offline, no API key, no network. Same input -> same result, forever.

WHAT THIS DOES NOT MEASURE: whether few-shot improves answer *quality*. That is
an efficacy claim and lives in ../../../data/techniques.yml with its sources.
This experiment only quantifies the price you pay in context, which is real,
linear in the number of examples, and almost always left uncounted.

Token counts are ESTIMATES from two documented heuristics in OpenAI's public
guidance (~4 characters per token; ~4/3 tokens per word). We report the band
between them. For exact counts use the target model's tokenizer — but the
*ratio* between variants, which is what this experiment is about, is stable
regardless of tokenizer.

Usage:
    python3 measure.py                 # table, defaults below
    python3 measure.py --json          # machine-readable
    python3 measure.py --price-per-1k 0.003 --calls 100000
"""
import argparse
import json

INSTRUCTION = "You are a careful annotator. Answer with a single word.\n\n"

TASK = (
    'Review: "The battery lasts all day and the screen is gorgeous."\n'
    "Sentiment:"
)

EXAMPLES = [
    ('Review: "It broke after two days."\nSentiment:', " negative"),
    ('Review: "Does exactly what it says on the box."\nSentiment:', " neutral"),
    ('Review: "Best purchase I have made all year!"\nSentiment:', " positive"),
    ('Review: "Shipping was slow but the product is fine."\nSentiment:', " neutral"),
    ('Review: "Stopped charging within a week, avoid."\nSentiment:', " negative"),
]

SHOT_COUNTS = (0, 1, 3, 5)


def estimate_tokens(text):
    """Return (low, high) token estimates from two documented heuristics."""
    by_chars = len(text) / 4.0
    by_words = len(text.split()) * 4.0 / 3.0
    return min(by_chars, by_words), max(by_chars, by_words)


def build_prompt(n_shots):
    parts = [INSTRUCTION]
    for question, answer in EXAMPLES[:n_shots]:
        parts.append(question + answer + "\n\n")
    parts.append(TASK)
    return "".join(parts)


def rows(price_per_1k, calls):
    out = []
    for n in SHOT_COUNTS:
        prompt = build_prompt(n)
        low, high = estimate_tokens(prompt)
        mid = (low + high) / 2.0
        out.append({
            "shots": n,
            "chars": len(prompt),
            "tokens_low": round(low),
            "tokens_high": round(high),
            "tokens_mid": round(mid),
            "usd": round(mid / 1000.0 * price_per_1k * calls, 2),
        })
    base = out[0]["tokens_mid"]
    for r in out:
        r["overhead_x"] = round(r["tokens_mid"] / base, 2)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--price-per-1k", type=float, default=0.003,
                    help="USD per 1K input tokens (default 0.003)")
    ap.add_argument("--calls", type=int, default=100000,
                    help="calls to project cost over (default 100000)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    data = rows(args.price_per_1k, args.calls)
    if args.json:
        print(json.dumps(data, indent=2))
        return

    hdr = f'{"shots":>5} | {"chars":>6} | {"tokens (est.)":>14} | {"x vs 0-shot":>11} | USD / {args.calls:,} calls'
    print(hdr)
    print("-" * len(hdr))
    for r in data:
        band = f'{r["tokens_low"]}-{r["tokens_high"]}'
        print(f'{r["shots"]:>5} | {r["chars"]:>6} | {band:>14} | {r["overhead_x"]:>10}x | ${r["usd"]:,.2f}')
    print()
    print(f'Assumes ${args.price_per_1k:.4f} per 1K input tokens over {args.calls:,} calls. '
          "Measures input cost only, not answer quality.")


if __name__ == "__main__":
    main()
