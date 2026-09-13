#!/usr/bin/env python3
"""Check that data/techniques.yml says what this repository promises it says.

    python3 scripts/validate-ledger.py

The first validator lived inline in the workflow and checked presence: every
entry has a grade, sources and a date. That let through a ledger with two
entries sharing an id, a "source" that is prose with no way to look it up, a
verification date in the future, a `see:` pointing at a file that is not there,
and a `reproducible: yes-offline` whose experiment measures token cost while the
row reads as if it measured quality. All of those are structural claims a reader
relies on, so all of them are checked now.

Standard library plus PyYAML, like the workflow. Every failure is listed, not
only the first.
"""
from __future__ import annotations

import datetime
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, "data", "techniques.yml")

REQUIRED = ["id", "question", "grade", "scope", "primary_sources", "reproducible", "last_verified", "see"]
GRADES = {"solid", "mixed", "folklore"}
REPRODUCIBLE = {"yes-offline", "yes-llm", "paper-only", "no"}
# What an experiment measures. Required whenever `reproducible` claims one
# exists: a row that says yes-offline and measures token cost must not read as
# if it measured accuracy. Audit finding E01.
EVIDENCE_TARGETS = {"cost", "quality", "format"}

# A primary source must be something a reader can resolve without guessing.
IDENTIFIER = re.compile(
    r"arXiv:\s*\d{4}\.\d{4,5}(v\d+)?"      # arXiv id
    r"|\b10\.\d{4,9}/\S+"                  # DOI
    r"|https?://\S+",                      # a URL
    re.I,
)


def main() -> int:
    problems: list[str] = []
    with open(LEDGER, encoding="utf-8") as fh:
        entries = yaml.safe_load(fh) or []
    if not isinstance(entries, list):
        print("data/techniques.yml must be a list of entries"); return 1

    today = datetime.date.today()
    seen_ids: dict[str, int] = {}
    for i, e in enumerate(entries):
        tag = str(e.get("id", f"entry #{i}"))
        for k in REQUIRED:
            if not e.get(k):
                problems.append(f"{tag}: missing '{k}'")

        ident = e.get("id")
        if ident in seen_ids:
            problems.append(f"{tag}: duplicate id (also entry #{seen_ids[ident]})")
        elif ident:
            seen_ids[ident] = i
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(ident)):
                problems.append(f"{tag}: id must be lowercase-kebab-case")

        if e.get("grade") not in GRADES:
            problems.append(f"{tag}: grade must be one of {sorted(GRADES)}, got {e.get('grade')!r}")

        rep = str(e.get("reproducible", ""))
        if rep not in REPRODUCIBLE:
            problems.append(f"{tag}: reproducible must be one of {sorted(REPRODUCIBLE)}, got {rep!r}")
        if rep.startswith("yes-"):
            if e.get("evidence_target") not in EVIDENCE_TARGETS:
                problems.append(f"{tag}: reproducible={rep} needs evidence_target in {sorted(EVIDENCE_TARGETS)} "
                                f"(what does the experiment measure?), got {e.get('evidence_target')!r}")
        elif e.get("evidence_target") not in (None, *EVIDENCE_TARGETS):
            problems.append(f"{tag}: evidence_target must be one of {sorted(EVIDENCE_TARGETS)}")

        ps = e.get("primary_sources")
        if not isinstance(ps, list) or not ps:
            problems.append(f"{tag}: primary_sources must be a non-empty list")
        else:
            for src in ps:
                if not IDENTIFIER.search(str(src)):
                    problems.append(f"{tag}: source has no arXiv id, DOI or URL to look it up: {str(src)[:60]!r}")
            if len(set(map(str, ps))) != len(ps):
                problems.append(f"{tag}: duplicate primary source")

        try:
            d = datetime.date.fromisoformat(str(e.get("last_verified", "")))
            if d > today:
                problems.append(f"{tag}: last_verified {d} is in the future")
        except ValueError:
            problems.append(f"{tag}: last_verified must be an ISO date (YYYY-MM-DD)")

        see = e.get("see")
        if see and not os.path.exists(os.path.join(ROOT, str(see).split("#")[0])):
            problems.append(f"{tag}: see points at a file that does not exist: {see}")

    if problems:
        sys.stderr.write(f"\nLedger validation FAILED — {len(problems)} problem(s):\n")
        for p in problems:
            sys.stderr.write(f"  - {p}\n")
        return 1
    n_exp = sum(1 for e in entries if str(e.get("reproducible", "")).startswith("yes-"))
    print(f"ledger OK: {len(entries)} entries, unique ids, every source resolvable, dates valid, "
          f"{n_exp} experiments with a declared evidence target")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
