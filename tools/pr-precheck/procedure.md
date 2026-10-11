# Procedure: how this tool grades a PR package

## Read order

1. Identify the mode and one package. Live: read scope first, validate the exact target repo, and stop on a placeholder or out-of-scope target; then read voice-guide separately. Eval: use only the frozen bundle and ignore both files.
2. Read rubric.md and references/evidence-guide.md. Refuse if rubric or procedure has no authored content.
3. Read Repo facts, Issue and Thread highlights before candidate claims. Live equivalents are the issue/thread, PR template and docs/CONTRIBUTING.md with applicable referenced policies. List stated asks without inventing absent policies.
4. Read Plan context, accepted repro, test plan, scope and deviations. Live: read the supplied plan.md and own posted repro, or supplied house plan/repro pack.
5. Read the candidate title, entire description, commit list, full diff and test evidence. Live use pr_draft.md, `git log main..HEAD --oneline`, `git diff main...HEAD` and test_evidence.md; do not substitute uncommitted working-tree edits.

## Evidence gathering

1. Make a Files ledger: every changed file and substantive hunk, paired with its plan item or recorded deviation. A named directory includes files beneath it; a requested changelog covers its entry. Record missing promised controls and unrelated cleanup separately.
2. Make a Claims ledger: every material title/description/checklist claim paired with actual diff or test proof. Read the whole diff for negative claims such as no options added. Distinguish a fixture's existence, its execution, and its result.
3. Pair the repro and plan test cases with reproducible commands/actions and concrete observed results. Include relevant controls, targeted tests and applicable repository commands. Accept explicit actual outcomes reported in prose or command annotations as well as stdout; do not mistake before/after observations for merely planned expectations. Named suite/control execution reports count without a full transcript when anchored by a concrete issue reproduction. Generic suite praise alone does not replace the planned trigger or controls. Record failures, skips and limitations literally.
4. Inspect every hunk for review debris, accidental changes, unrelated refactors and necessary broad changes. Do not fail solely on length or commit count.
5. Make a Standards ledger listing each applicable stated template, changelog/docs, contribution or AI-disclosure obligation and its satisfaction or omission. Where no policy exists, record absence, not failure. Live voice notes remain separate.

## Check execution

1. Grade all six rubric rows in table order, applying the exact pass condition to the ledgers.
2. Use pass for supported satisfaction, fail for a contradiction or clearly missing required element, and unclear for genuine ambiguity or insufficient evidence. Give a deciding fact or quote and its source for each grade.
3. Recognize explicit scoped-down work and honest failing commands without equating less-than-everything with unreadiness. However, disclosure does not legitimize unrelated cleanup or waive mandatory standards.
4. If evidence is insufficient, reread the relevant supplied artifact. Never fetch outside a frozen bundle, infer a test ran from its fixture, infer AI use from style, or rewrite the rubric during grading. Report procedure gaps in the summary.

## Verdict assembly

1. All required pass gives accept; any required fail or unclear gives reject. Preferred grades and live voice notes cannot override this rule.
2. Summarize all checks, deciding evidence and concrete repairs for blockers. Keep advisory concerns separate and do not claim a repair was executed.
3. End with exactly the SKILL.md fenced JSON schema: item, checks (name, grade, evidence), verdict. Include every row once in order, using the bundle id or PR/issue URL. Nothing follows the JSON.
