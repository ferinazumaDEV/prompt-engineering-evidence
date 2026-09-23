# Folklore, debunked

Prompt "tricks" that circulate widely with no reproducible evidence — or that were actively debunked. For each: the claim, why it spread, what the evidence says, and the verdict. Same rule as the rest of the repo: **a claim without a source is not a fact.**

> Why this page exists: the harm of folklore isn't just wasted effort — it's that people build systems on it. A grade of `folklore` here means *"stop paying attention to this and spend the effort on evals instead."*

---

## <a id="deep-breath"></a> "Take a deep breath" (and other motivational phrases)

**Claim:** telling the model to "take a deep breath and work step by step" boosts accuracy.
**Why it spread:** it comes from a real paper — Google's OPRO (Yang et al. 2023, arXiv:2309.03409) *searched* for optimal instruction strings and found this one scored highest **for PaLM-2-L on GSM8K**. The internet dropped the "for one specific model, found by automated search" part.
**Evidence:** it's a model-specific optimum, not a general principle. It does not reliably transfer across models or tasks, and there's no evidence the *emotional framing* is what helps.
**Verdict:** **folklore.** If you want the CoT benefit, just ask for step-by-step reasoning (see [chain-of-thought](data/techniques.yml)); the "deep breath" adds nothing portable.

## <a id="threats-tips"></a> Threats, tipping, and "my job depends on this"

**Claim:** threatening the model, offering it $200, or claiming stakes improves output.
**Why it spread:** viral screenshots and single-run anecdotes; occasionally a real but tiny, non-reproducible bump on one model version.
**Evidence:** a controlled study (Meincke et al. 2025, Prompting Science Report 3, [arXiv:2508.00614](https://arxiv.org/abs/2508.00614)) finds no significant benchmark effect from tipping or threatening on GPQA / MMLU-Pro; per-question effects vary in both directions. Beyond that, results are anecdotal, model- and version-specific, and vanish on model updates. Newer instruction-tuned models are largely flat to it (same study). The tipping principle traces to Bsharat et al. 2023 ([arXiv:2312.16171](https://arxiv.org/abs/2312.16171)).
**Verdict:** **folklore.** Spend the tokens on clear instructions and examples instead.

## <a id="temperature-zero"></a> "Temperature 0 makes the model deterministic"

**Claim:** set temperature to 0 and you get identical output every time.
**Why it spread:** temperature 0 *does* make sampling greedy, so it feels deterministic in small tests.
**Evidence:** greedy sampling removes one source of randomness, but **not all of them**: batching, mixture-of-experts routing, floating-point/hardware nondeterminism, and provider-side changes can still vary the output. Vendors document that identical output is not guaranteed — Anthropic's [Messages API reference](https://platform.claude.com/docs/en/api/messages): *"even with `temperature` of `0.0`, the results will not be fully deterministic"*.
**Verdict:** **folklore** (as an absolute). Temp 0 reduces variance; it does not guarantee determinism. For reproducibility, pin the model version and record outputs — don't assume.
**Update 2026-09-23:** Google now steers away from tuning temperature at all on its reasoning models: "For all Gemini 3 models, we strongly recommend keeping the temperature parameter at its default value of 1.0" (Source: Google, Gemini 3 developer guide, vendor documentation)(https://ai.google.dev/gemini-api/docs/gemini-3). Temperature 0 is not only non-deterministic; on this model family the vendor no longer recommends it.

## <a id="role-prompting"></a> "Assigning an expert role boosts accuracy"

**Claim:** "You are an expert mathematician" makes the model better at math.
**Why it spread:** role prompts *do* shape tone, vocabulary, and format convincingly, so it feels like it must help correctness too.
**Evidence:** persona/role prompts reliably affect *style*, but studies find little to no consistent effect on *accuracy* on objective tasks (see Zheng et al. 2024, "When 'A Helpful Assistant' Is Not Really Helpful", arXiv:2311.10054).
**Verdict:** **folklore** (for accuracy; style effects are real). Use roles to control voice and audience; do not expect them to fix reasoning. That's what evals and the right technique are for.
**Update 2026-09-23:** two further preprints point the same way. Across six models on GPQA Diamond and MMLU-Pro, "persona prompts generally did not improve accuracy relative to a no-persona baseline"; domain-mismatched expert personas sometimes degrade performance and low-knowledge personas often reduce accuracy (Source: Basil et al. 2025, Prompting Science Report 4, preprint)(https://arxiv.org/abs/2512.05858). On 1,140 open-ended questions across 38 expert roles, role prompting raises judged expertise depth while reducing clarity, and "primarily reshapes response characteristics rather than broadly improving capability" (Source: Xiao et al. 2026, preprint)(https://arxiv.org/abs/2605.29420). The style effect is measurable; the accuracy gain is not.

## <a id="json-reasoning"></a> "Forcing JSON output is free"

**Claim:** constraining the model to strict JSON has no downside.
**Why it spread:** structured output is so useful for pipelines that people assume it's cost-free.
**Evidence:** heavy format constraints can *reduce* reasoning quality on some tasks — the model spends capacity satisfying the schema (Tam et al. 2024, "Let Me Speak Freely?", arXiv:2408.02442). Mitigation: let the model reason first (a `reasoning` field before the answer), or reason in prose then convert.
**Verdict:** **mixed.** Structured output is great; "free" is wrong. Put a reasoning step before the constrained answer.

## <a id="xml-magic"></a> "XML tags are magic for Claude"

**Claim:** wrapping everything in XML tags unlocks hidden performance.
**Why it spread:** Anthropic *does* recommend XML tags, and they genuinely help.
**Evidence:** they help because they **disambiguate structure** (which text is the data, which is the instruction), not because the model has a special XML mode. Any consistent, unambiguous delimiter achieves the same; XML is just a clean, common choice.
**Verdict:** **mixed** (delimiters help; XML-specific magic is folklore). Use delimiters for clarity; the win is structure, not the angle brackets.

## <a id="politeness"></a> "Be polite to the model" / "Be rude to the model"

*Added 2026-09-23.*

**Claim:** saying "please" (or, in the 2025 variant, being blunt or rude) makes answers more accurate.
**Why it spread:** a short paper on one model found rude prompts scoring higher, and the headline travelled without the sample size; the older "be polite" rule travelled the same way.
**Evidence:** the effect exists, but its sign, size and significance move with model, domain and language. On ChatGPT-4o with 50 base questions rewritten into five tones, accuracy ranged from 80.8 percent for Very Polite to 84.8 percent for Very Rude prompts (Source: Dobariya and Kumar 2025, preprint, short paper)(https://arxiv.org/abs/2510.04950). On MMMLU with GPT-4o mini, Gemini 2.0 Flash and Llama 4 Scout, neutral or very polite prompts generally score higher than very rude ones, but significant effects appear only in a subset of Humanities tasks and largely lose significance when aggregated (Source: Cai et al. 2025, preprint)(https://arxiv.org/abs/2512.12812). Across English, Hindi and Spanish and five models, polite prompts raise judged response quality by up to about 11 percent and impolite tones lower it, yet "these effects are neither consistent nor universal across languages and models"; the metric there is judged quality, not benchmark accuracy (Source: Mehta et al. 2026, preprint)(https://arxiv.org/abs/2604.16275). On a 570-question MMLU subset with seven tone variants across four models including ChatGPT-5-nano, "tonal effects are systematic but highly model-dependent" (Source: Dobariya and Kumar 2026, preprint)(https://arxiv.org/abs/2605.29027). The earliest controlled look already said the same: "sometimes being polite to the LLM helps performance, and sometimes it lowers performance" (Source: Meincke et al. 2025, Prompting Science Report 1, preprint)(https://arxiv.org/abs/2503.04818).
**Verdict:** **mixed**, not a technique. Tone is a real input that your eval should hold constant; it is not a lever you can pull in one direction and expect a portable gain. No ledger row yet: adding one changes the archived counts and is a maintainer decision (see [`CLAIMS.md`](CLAIMS.md)).

---

*Think a verdict here is wrong? Open a "challenge a grade" issue with your evidence — that's how this stays honest.*
