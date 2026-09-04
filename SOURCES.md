# Sources

Primary sources behind the graded ledger. Papers are linked by arXiv ID; vendor docs and concepts by name. If a claim in this repo doesn't trace to something here (or to a reproducible experiment), it's a bug — open an issue.

## Reasoning

- **Chain-of-Thought** — Wei et al. 2022, *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* — [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- **When CoT helps (and doesn't)** — Sprague et al. 2024, *To CoT or not to CoT?* — [arXiv:2409.12183](https://arxiv.org/abs/2409.12183)
- **Self-Consistency** — Wang et al. 2022, *Self-Consistency Improves Chain of Thought Reasoning* — [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- **CoT on reasoning models (marginal gains, more tokens)** — Meincke et al. 2025, *Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting* — [arXiv:2506.07142](https://arxiv.org/abs/2506.07142)

## Fundamentals

- **Few-shot / in-context learning** — Brown et al. 2020, *Language Models are Few-Shot Learners* — [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- **Example-order sensitivity** — Lu et al. 2021, *Fantastically Ordered Prompts and Where to Find Them* — [arXiv:2104.08786](https://arxiv.org/abs/2104.08786)
- **Lost in the middle** — Liu et al. 2023, *Lost in the Middle: How Language Models Use Long Contexts* — [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)

## Output control

- **Format constraints vs reasoning** — Tam et al. 2024, *Let Me Speak Freely?* — [arXiv:2408.02442](https://arxiv.org/abs/2408.02442)

## Folklore / null effects

- **OPRO ("take a deep breath")** — Yang et al. 2023, *Large Language Models as Optimizers* — [arXiv:2309.03409](https://arxiv.org/abs/2309.03409)
- **Role prompting ≠ accuracy** — Zheng et al. 2024, *When "A Helpful Assistant" Is Not Really Helpful* — [arXiv:2311.10054](https://arxiv.org/abs/2311.10054)
- **Threats and tips (null result)** — Meincke et al. 2025, *Prompting Science Report 3: I'll pay you or I'll kill you — but will you care?* — [arXiv:2508.00614](https://arxiv.org/abs/2508.00614)
- **Tipping principle (origin)** — Bsharat et al. 2023, *Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4* — [arXiv:2312.16171](https://arxiv.org/abs/2312.16171)
- **Nondeterminism at temperature 0** — He, H. and Thinking Machines Lab 2025, *Defeating Nondeterminism in LLM Inference* — [thinkingmachines.ai](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Security

- **Indirect prompt injection** — Greshake et al. 2023, *Not What You've Signed Up For* — [arXiv:2302.12173](https://arxiv.org/abs/2302.12173)
- **Prompt injection (term, 2022)** — Simon Willison, *Prompt injection attacks against GPT-3* — [simonwillison.net](https://simonwillison.net/2022/Sep/12/prompt-injection/)
- **Dual-LLM pattern (2023)** — Simon Willison, *The Dual LLM pattern for building AI assistants that can resist prompt injection* — [simonwillison.net](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/)
- **The lethal trifecta (2025)** — Simon Willison, *The lethal trifecta for AI agents* — [simonwillison.net](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- **Prompt injection, ongoing coverage** — Simon Willison, [simonwillison.net/tags/prompt-injection](https://simonwillison.net/tags/prompt-injection/)
- **CaMeL (capability-based defence)** — Debenedetti et al. 2025, *Defeating Prompt Injections by Design* — [arXiv:2503.18813](https://arxiv.org/abs/2503.18813)
- **OWASP Top 10 for LLM Applications** — LLM01: Prompt Injection — [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## Vendor documentation

- **Anthropic** — prompt engineering docs — [platform.claude.com/docs](https://platform.claude.com/docs)
  - *Long context prompting* ("up to 30 percent in tests" with the query at the end) — [claude-prompting-best-practices#long-context-prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#long-context-prompting)
  - *Be clear and direct* ("tell Claude what to do instead of what not to do") — [claude-prompting-best-practices#be-clear-and-direct](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct)
  - *Structure prompts with XML tags* — [claude-prompting-best-practices#structure-prompts-with-xml-tags](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#structure-prompts-with-xml-tags)
  - *Messages API reference*, `temperature` ("even with temperature of 0.0, the results will not be fully deterministic") — [docs/en/api/messages](https://platform.claude.com/docs/en/api/messages)
- **OpenAI** — prompting guide — [platform.openai.com/docs](https://platform.openai.com/docs)
  - *Reasoning best practices* ("Avoid chain-of-thought prompts" for reasoning models; CoT "can sometimes hinder") — [developers.openai.com](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
  - *Reproducible outputs with the seed parameter* (OpenAI Cookbook; determinism "is not guaranteed") — [developers.openai.com/cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter)
  - *Best practices for prompt engineering with the OpenAI API* (Help Center; "say what to do instead") — [help.openai.com](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api) — needs-verification: the page answers 403 to command-line fetches, check it in a browser

> Dates and exact numbers move with model versions. Where this repo cites a measured figure, it is a dated snapshot — re-run the experiment to refresh.
