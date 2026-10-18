# Search strategy: where my scout looks, and why

## Queries

Union these separate queries; do not intersect them. The TypeScript/JavaScript defaults come from my actual web/document project, not the activity's sample Python profile. The `updated` sort defines the fetched 100-result window; it is not the entire GitHub result set.

Q1 — Profile: “My current Verdean project uses TypeScript/JavaScript, React, Node.js, JSON-oriented document-intelligence routes, and regression tests”; “I want a bounded first contribution ... rather than an open-ended redesign.”
```sh
gh search issues --language TypeScript --label 'good first issue' --state open --limit 100 --archived=false --visibility public --sort updated --order desc --json title,repository,labels,assignees,commentsCount,updatedAt,url,state,isPullRequest
```

Q2 — Same profile sentence, JavaScript half. The beginner label supports discovery, not a scope or availability verdict.
```sh
gh search issues --language JavaScript --label 'good first issue' --state open --limit 100 --archived=false --visibility public --sort updated --order desc --json title,repository,labels,assignees,commentsCount,updatedAt,url,state,isPullRequest
```

Q3 — Profile: “Prefer document ingestion, LLM-output handling, or agent-tool bugs with explicit inputs and expected outputs”; target JSON in TypeScript bug reports without requiring a beginner label.
```sh
gh search issues json --language TypeScript --label bug --state open --limit 100 --archived=false --visibility public --sort updated --order desc --json title,repository,labels,assignees,commentsCount,updatedAt,url,state,isPullRequest
```

Q4 — Same document/agent profile sentence; target document bugs in JavaScript.
```sh
gh search issues document --language JavaScript --label bug --state open --limit 100 --archived=false --visibility public --sort updated --order desc --json title,repository,labels,assignees,commentsCount,updatedAt,url,state,isPullRequest
```

## Ranking filters

Apply in this order using only the query JSON. No issue/thread fetch or model judgment belongs in ranking. `rank_candidates.py` implements these rules, saving counts, drop reasons, query provenance, the whole survivor list, and the top five.

1. Combine Q1–Q4 in that order and dedupe by exact issue URL. Keep the first record for a duplicate and union its query IDs (sorted). Record metadata disagreements rather than silently merging contradictory fields.
2. Drop non-open records, pull requests, records with any assignee, and records whose `updatedAt` is more than 90 days before the saved UTC capture timestamp (boundary inclusive). Missing fields are errors, not inferred negatives.
3. From the case-insensitive title alone, prefer a whole-word match for `json`, `document`, `documents`, `pdf`, `ingestion`, `parser`, `parsing`, `llm`, `agent`, `agents`, `tool`, or `tools`. These are profile keywords, not scope verdicts.
4. Within each relevance group, prefer an exact case-insensitive `bug` label, then prefer an exact `good first issue` label.
5. Then order by fewest comments first, newest `updatedAt` first, and exact URL lexicographically ascending. This is a total ordering, independent of search-return order except the explicit duplicate rule.
6. Take exactly five survivors. If fewer survive, stop and revise the authored strategy; never silently lower N or pad the scan.

Labels and update dates only triage cheaply. A fresh update could be a claim; maintainers, true boundedness, claims/open PRs, and AI policies must still be checked during grading. This is a practice GitHub scan, not permission to choose an issue outside the course site.

## How many to grade

Grade the top **5** ranked results per scan. Save the actual complete summary through final JSON to `scan-output.md`; append the separate direct grading of 2–3 course-site picks below it. Use only the verified work/CodePath Claude account, never personal billing as a fallback.
