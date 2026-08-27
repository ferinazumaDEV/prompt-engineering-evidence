# Contributing

This reference has one non-negotiable rule.

## Every claim carries a grade, a source, and evidence — or it doesn't go in.

For any technique or claim you add or change:

1. **Grade it:** `solid` / `mixed` / `folklore` (see the [README](README.md) for definitions).
2. **Cite a primary source:** a paper (arXiv/DOI), official vendor docs, or a reproducible experiment in this repo. No blog-of-a-blog, no *"everyone knows"*.
3. **State the scope:** where it applies and where it doesn't. A technique with no scope is a red flag.
4. **Date it:** `last_verified` (ISO date). Model-measured numbers are **snapshots**, not eternal truths — always *"as of DATE on MODEL"*.

Entries in [`data/techniques.yml`](data/techniques.yml) that lack `grade` + `primary_sources` + `last_verified` **fail CI** and cannot be merged.

## Challenge a grade

Think a grade is wrong? Open a **"challenge a grade"** issue with your evidence. Disagreement *backed by sources* is how this stays honest — and it's welcome.

## What does NOT belong here

- "Act as X" persona prompts or prompt dumps — this is not a prompt library.
- Claims of big effects with no reproducible source (*"+30% with this one trick"*).
- Beginner tutorials — link to [learnprompting.org](https://learnprompting.org) instead.
