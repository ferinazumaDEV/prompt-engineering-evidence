# Sources

Primary sources behind the graded ledger. Papers are linked by arXiv ID; vendor docs and concepts by name. If a claim in this repo doesn't trace to something here (or to a reproducible experiment), it's a bug — open an issue.

## Reasoning

- **Chain-of-Thought** — Wei et al. 2022, *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* — [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- **When CoT helps (and doesn't)** — Sprague et al. 2024, *To CoT or not to CoT?* — [arXiv:2409.12183](https://arxiv.org/abs/2409.12183)
- **Self-Consistency** — Wang et al. 2022, *Self-Consistency Improves Chain of Thought Reasoning* — [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- **CoT on reasoning models (marginal gains, more tokens)** — Meincke et al. 2025, *Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting* — [arXiv:2506.07142](https://arxiv.org/abs/2506.07142)
- **Majority-vote failure mode (self-consistency)** — Cai et al. 2026, *ARBITER: Reasoning Trajectory Basins and Majority Vote Failures in Test-Time Sampling* — [arXiv:2605.26172](https://arxiv.org/abs/2605.26172) — added 2026-09-23

## Fundamentals

- **Few-shot / in-context learning** — Brown et al. 2020, *Language Models are Few-Shot Learners* — [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- **Example-order sensitivity** — Lu et al. 2021, *Fantastically Ordered Prompts and Where to Find Them* — [arXiv:2104.08786](https://arxiv.org/abs/2104.08786)
- **Lost in the middle** — Liu et al. 2023, *Lost in the Middle: How Language Models Use Long Contexts* — [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- **Positional bias at high context utilisation** — Veseli et al. 2025, *Positional Biases Shift as Inputs Approach Context Window Limits* — [arXiv:2508.07479](https://arxiv.org/abs/2508.07479) — added 2026-09-23

## Output control

- **Format constraints vs reasoning** — Tam et al. 2024, *Let Me Speak Freely?* — [arXiv:2408.02442](https://arxiv.org/abs/2408.02442)

## Folklore / null effects

- **OPRO ("take a deep breath")** — Yang et al. 2023, *Large Language Models as Optimizers* — [arXiv:2309.03409](https://arxiv.org/abs/2309.03409)
- **Role prompting ≠ accuracy** — Zheng et al. 2024, *When "A Helpful Assistant" Is Not Really Helpful* — [arXiv:2311.10054](https://arxiv.org/abs/2311.10054)
- **Expert personas ≠ factual accuracy (six models, GPQA Diamond / MMLU-Pro)** — Basil et al. 2025, *Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy* — [arXiv:2512.05858](https://arxiv.org/abs/2512.05858) — added 2026-09-23
- **Personas reshape style and depth, not capability** — Xiao et al. 2026, *When Does Persona Prompting Actually Help? A Retrieval and Metric Analysis of Expert Role Injection in LLMs* — [arXiv:2605.29420](https://arxiv.org/abs/2605.29420) — added 2026-09-23
- **Prompting effects are contingent (politeness helps sometimes, hurts sometimes)** — Meincke et al. 2025, *Prompting Science Report 1: Prompt Engineering is Complicated and Contingent* — [arXiv:2503.04818](https://arxiv.org/abs/2503.04818) — added 2026-09-23
- **Threats and tips (null result)** — Meincke et al. 2025, *Prompting Science Report 3: I'll pay you or I'll kill you — but will you care?* — [arXiv:2508.00614](https://arxiv.org/abs/2508.00614)
- **Tipping principle (origin)** — Bsharat et al. 2023, *Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4* — [arXiv:2312.16171](https://arxiv.org/abs/2312.16171)
- **Nondeterminism at temperature 0** — He, H. and Thinking Machines Lab 2025, *Defeating Nondeterminism in LLM Inference* — [thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Tone and politeness

Added 2026-09-23. Four preprints, none peer-reviewed; they disagree on the sign of the effect and agree that it is model-dependent.

- **Rude beats polite on one model (n = 50 questions, ChatGPT-4o)** — Dobariya and Kumar 2025, *Mind Your Tone: Investigating How Prompt Politeness Affects LLM Accuracy (short paper)* — [arXiv:2510.04950](https://arxiv.org/abs/2510.04950)
- **Polite or neutral beats rude, significant only in some Humanities tasks (GPT-4o mini, Gemini 2.0 Flash, Llama 4 Scout)** — Cai et al. 2025, *Does Tone Change the Answer? Evaluating Prompt Politeness Effects on Modern LLMs: GPT, Gemini, and LLaMA* — [arXiv:2512.12812](https://arxiv.org/abs/2512.12812)
- **Cross-lingual (English, Hindi, Spanish), five models, judged quality not accuracy** — Mehta et al. 2026, *No Universal Courtesy: A Cross-Linguistic, Multi-Model Study of Politeness Effects on LLMs Using the PLUM Corpus* — [arXiv:2604.16275](https://arxiv.org/abs/2604.16275)
- **Seven tone variants, 570 MMLU questions, four models incl. ChatGPT-5-nano** — Dobariya and Kumar 2026, *Mind Your Tone: Does Tone Alter LLM Performance?* — [arXiv:2605.29027](https://arxiv.org/abs/2605.29027)

## Security

- **Indirect prompt injection** — Greshake et al. 2023, *Not What You've Signed Up For* — [arXiv:2302.12173](https://arxiv.org/abs/2302.12173)
- **Prompt injection (term, 2022)** — Simon Willison, *Prompt injection attacks against GPT-3* — [simonwillison.net](https://simonwillison.net/2022/Sep/12/prompt-injection/)
- **Dual-LLM pattern (2023)** — Simon Willison, *The Dual LLM pattern for building AI assistants that can resist prompt injection* — [simonwillison.net](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/)
- **The lethal trifecta (2025)** — Simon Willison, *The lethal trifecta for AI agents* — [simonwillison.net](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- **Prompt injection, ongoing coverage** — Simon Willison, [simonwillison.net/tags/prompt-injection](https://simonwillison.net/tags/prompt-injection/)
- **CaMeL (capability-based defence)** — Debenedetti et al. 2025, *Defeating Prompt Injections by Design* — [arXiv:2503.18813](https://arxiv.org/abs/2503.18813)
- **OWASP Top 10 for LLM Applications** — LLM01: Prompt Injection — [genai.owasp.org](https://genai.owasp.org/llm-top-10/)
- **Injection susceptibility of LLM graders (2025–2026 models)** — Wanjura, Meincke et al. 2026, *Prompting Science Report 5: This is an Excellent Paper: The Effects of Prompt Injection on Grading* — Wharton Generative AI Labs technical report, [gail.wharton.upenn.edu](https://gail.wharton.upenn.edu/research-and-insights/hidden-prompt-injections/) — lab report, not peer-reviewed; the SSRN copy (abstract id 6510758) answers 403 to command-line fetches; no arXiv version found — added 2026-09-23

## Vendor documentation

- **Anthropic** — prompt engineering docs — [platform.claude.com/docs](https://platform.claude.com/docs)
  - *Long context prompting* ("up to 30 percent in tests" with the query at the end) — [claude-prompting-best-practices#long-context-prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#long-context-prompting) — re-read 2026-09-23, wording unchanged
  - *Be clear and direct* ("tell Claude what to do instead of what not to do") — [claude-prompting-best-practices#be-clear-and-direct](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct) — re-read 2026-09-23, wording unchanged; the same page now says "Include 3–5 examples for best results" and, for Claude Opus 5, that verification instructions carried over from earlier prompts "can cause over-verification, adding tokens and latency"
  - *Prompting Claude Opus 5.5* ("effort is the main control"; consider removing "think carefully before answering" instructions in chat system prompts) — [prompting-claude-opus-5-5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) — added 2026-09-23
  - *Structure prompts with XML tags* — [claude-prompting-best-practices#structure-prompts-with-xml-tags](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#structure-prompts-with-xml-tags)
  - *Messages API reference*, `temperature` ("even with temperature of 0.0, the results will not be fully deterministic") — [docs/en/api/messages](https://platform.claude.com/docs/en/api/messages)
- **OpenAI** — prompting guide — [platform.openai.com/docs](https://platform.openai.com/docs)
  - *Reasoning best practices* ("Avoid chain-of-thought prompts" for reasoning models; CoT "can sometimes hinder") — [developers.openai.com](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — re-read 2026-09-23: wording unchanged; the page names o3, o4-mini and GPT-4.1 as its examples and does not name GPT-5-class models; it also says "try to write prompts without examples first" on reasoning models
  - *Reproducible outputs with the seed parameter* (OpenAI Cookbook; determinism "is not guaranteed") — [developers.openai.com/cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter)
  - *Best practices for prompt engineering with the OpenAI API* (Help Center; "say what to do instead") — [help.openai.com](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api) — needs-verification: the page answers 403 to command-line fetches, check it in a browser — verified via an Internet Archive capture of 2026-09-15 (page header "Updated: last month"), opened 2026-09-23 with rule 7 present: [web.archive.org](https://web.archive.org/web/20260915104022id_/https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- **Google** — Gemini API docs — added 2026-09-23. Both pages answer a 302 to a Google sign-in when fetched with a browser User-Agent and 200 with a plain `curl` User-Agent; the "Last updated" stamp is printed on each page.
  - *Prompt design strategies* ("We recommend to always include few-shot examples in your prompts"; "supply all the context first. Place your specific instructions or questions at the very end of the prompt") — [ai.google.dev](https://ai.google.dev/gemini-api/docs/prompting-strategies) — page stamp "Last updated 2026-09-17 UTC"
  - *Gemini 3 developer guide* (`thinking_level` in place of chain-of-thought prompting; "we strongly recommend keeping the temperature parameter at its default value of 1.0") — [ai.google.dev](https://ai.google.dev/gemini-api/docs/gemini-3) — page stamp "Last updated 2026-09-23 UTC" when read

> Dates and exact numbers move with model versions. Where this repo cites a measured figure, it is a dated snapshot — re-run the experiment to refresh.
