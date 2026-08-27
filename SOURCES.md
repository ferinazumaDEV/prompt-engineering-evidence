# Sources

Primary sources behind the graded ledger. Papers are linked by arXiv ID; vendor docs and concepts by name. If a claim in this repo doesn't trace to something here (or to a reproducible experiment), it's a bug — open an issue.

## Reasoning

- **Chain-of-Thought** — Wei et al. 2022, *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* — [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- **When CoT helps (and doesn't)** — Sprague et al. 2024, *To CoT or not to CoT?* — [arXiv:2409.12183](https://arxiv.org/abs/2409.12183)
- **Self-Consistency** — Wang et al. 2022, *Self-Consistency Improves Chain of Thought Reasoning* — [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)

## Fundamentals

- **Few-shot / in-context learning** — Brown et al. 2020, *Language Models are Few-Shot Learners* — [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- **Example-order sensitivity** — Lu et al. 2021, *Fantastically Ordered Prompts and Where to Find Them* — [arXiv:2104.08786](https://arxiv.org/abs/2104.08786)
- **Lost in the middle** — Liu et al. 2023, *Lost in the Middle: How Language Models Use Long Contexts* — [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)

## Output control

- **Format constraints vs reasoning** — Tam et al. 2024, *Let Me Speak Freely?* — [arXiv:2408.02442](https://arxiv.org/abs/2408.02442)

## Folklore / null effects

- **OPRO ("take a deep breath")** — Yang et al. 2023, *Large Language Models as Optimizers* — [arXiv:2309.03409](https://arxiv.org/abs/2309.03409)
- **Role prompting ≠ accuracy** — Zheng et al. 2024, *When "A Helpful Assistant" Is Not Really Helpful* — [arXiv:2311.10054](https://arxiv.org/abs/2311.10054)

## Security

- **Indirect prompt injection** — Greshake et al. 2023, *Not What You've Signed Up For* — [arXiv:2302.12173](https://arxiv.org/abs/2302.12173)
- **Prompt injection (term) & lethal trifecta & Dual-LLM** — Simon Willison, [simonwillison.net](https://simonwillison.net/tags/prompt-injection/)
- **OWASP Top 10 for LLM Applications** — LLM01: Prompt Injection — [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## Vendor documentation

- **Anthropic** — prompt engineering docs — [platform.claude.com/docs](https://platform.claude.com/docs)
- **OpenAI** — prompting guide — [platform.openai.com/docs](https://platform.openai.com/docs)

> Dates and exact numbers move with model versions. Where this repo cites a measured figure, it is a dated snapshot — re-run the experiment to refresh.
