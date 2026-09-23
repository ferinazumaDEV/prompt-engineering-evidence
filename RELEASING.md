# Releasing

A release of this repository is not a software release. It is a **citable version**: the tag becomes an archived
deposit on Zenodo with its own DOI, and that deposit is what someone cites, downloads and checks a grade against.
Everything below exists so that the deposit and the tag cannot drift apart.

## The rule that is different here

**In this repository you create the GitHub Release by hand. That is the step that mints the DOI.**

There is no `release.yml`. The Zenodo integration is a repository webhook subscribed to the `release` event: it
fires when the Release is published, takes a snapshot of the tag, and mints a version DOI.

This is the **opposite** of the rule in the five package repositories (`typedout`, `politeclient`, `scaffld`,
`webhook-replay`, `framesig`), where `release.yml` creates the Release itself and creating it by hand breaks the
run *after* it has already published to PyPI. Getting the two backwards is how two package releases had to be
repaired by hand on 14 September 2026. Before releasing anything, check which kind of repository you are in:

| | this repository | a package repository |
|---|---|---|
| has `.github/workflows/release.yml` | no | yes |
| who creates the GitHub Release | **you** | the workflow |
| what the tag triggers | nothing | the whole release run |
| what the Release triggers | the Zenodo deposit | nothing |

## When a release is warranted

Publish a version when the change **reaches a reader**: a grade that moved, a new entry, a primary source that
replaced a secondary one, a claim withdrawn. Continuous integration, internal tooling, formatting and dependency
pins do not reach a reader and do not justify a version.

A grade change is the strongest reason of all, because the whole point of the ledger is that someone can cite the
state of the evidence on a date.

`main` sitting ahead of the latest tag is therefore a normal, deliberate state, not a backlog.

## Steps

### 1. The preparation pull request

One pull request that moves every version string at once. In this repository the version lives in four places:

| file | what to change |
|---|---|
| `CITATION.cff` | `version:` and `date-released:` (the release date, ISO `YYYY-MM-DD`) |
| `about.jsonld` | the `"version"` field |
| `README.md` | the `Version` row of the table, which also names the release |
| `CHANGELOG.md` | promote `## [Unreleased]` to `## [X.Y.Z] — YYYY-MM-DD` and open a fresh `## [Unreleased]` |

Two things that have failed before and will fail again:

- **Do not link the tag from the README.** `releases/tag/vX.Y.Z` does not exist while the pull request is open, so
  the link check fails on the very pull request that prepares the release. Link the releases page instead, which
  never 404s and always shows the newest version.
- **Keep every scalar in `CITATION.cff` a scalar.** A list where a string is expected (a `license:` written as a
  list, for instance) makes the deposit fail its own metadata validation. This happened to the cookbook's v0.1.0
  on 4 September 2026.

### 2. Merge, and let CI finish on `main`

`ledger-validate`, `Link check` and `translations` all have to be green on `main`. Do not tag a commit whose
checks have not completed.

### 3. Create the tag on the merge commit

```
gh api -X POST repos/ferinazumaDEV/prompt-engineering-evidence/git/refs \
  -f ref=refs/tags/vX.Y.Z -f sha=<merge sha>
```

Nothing happens yet. In this repository the tag is a label, not a trigger.

### 4. Publish the GitHub Release — this mints the DOI

```
gh release create vX.Y.Z -R ferinazumaDEV/prompt-engineering-evidence \
  --title "vX.Y.Z" --notes-file <notes>
```

The notes say what changed for a reader, in the words of the changelog entry, and nothing about the tooling.

### 5. Verify at the destination, not at the sender

A published Release is not evidence that the deposit exists. Ask Zenodo:

```
python3 - <<'PY'
import json, urllib.request
rid = "22307826"   # concept record id for this work
req = urllib.request.Request(f"https://zenodo.org/api/records/{rid}",
                             headers={"User-Agent": "Mozilla/5.0 (compatible; release-check/1.0)"})
d = json.load(urllib.request.urlopen(req, timeout=40))
print(d["metadata"]["version"], d["doi"], d.get("conceptdoi"))
PY
```

`metadata.version` must equal the tag you just pushed, and `doi` is the new version DOI. The concept DOI
(`10.5281/zenodo.22307826`), which is what `CITATION.cff` carries, stays the same forever and always resolves to
the newest version — that is why it is the one to cite.

Two ways this check has misled before, both worth knowing:

- Querying `zenodo.org/api/records?q=doi:"..."` with the concept DOI returns **zero hits**, because the concept
  DOI is not any single record's `doi` field. Zero hits there proves nothing. Fetch the record by id instead.
- The repository's webhook delivery log can be empty even for a delivery that succeeded. It is not evidence
  either way. Zenodo is the destination; ask Zenodo.

Then check the deposit against the tag **by content**: every file in the archive must have the same SHA-256 as
the file at that tag. A DOI that resolves says a deposit exists, not that it contains what you tagged.

### 6. Software Heritage

Zenodo forwards the archive, but indexing is not immediate and the origin API returns `NotFoundExc` while it
catches up — a false negative, not a missing deposit. To be sure, trigger it and record the result in the release
notes:

```
curl -s -X POST "https://archive.softwareheritage.org/api/1/origin/save/git/url/https://github.com/ferinazumaDEV/prompt-engineering-evidence/"
```

2026-09-23: the latest full visit of this origin on Software Heritage is dated 2026-09-14, read from the origin visit
API below with a plain `curl` User-Agent (a browser User-Agent is served a bot-challenge page instead of JSON). When a
newer tag is expected to be archived, the save request above is the step; the visit date is the check that it worked.

```
curl -s -A curl/8.5.0 "https://archive.softwareheritage.org/api/1/origin/https://github.com/ferinazumaDEV/prompt-engineering-evidence/visit/latest/?require_snapshot=true"
```

## Never

- **Never delete a release.** Deleting one is what left Zenodo returning `409` with no DOI. It is not undoable by
  retrying.
- **Never edit a published deposit** to fix something. Publish the next version; the point of an archive is that
  the cited object does not move.
- **Never downgrade a grade silently.** If evidence moves an entry from `solid` to `mixed`, the changelog says
  which source moved it. A ledger whose grades change without a trail is an opinion with a DOI.
