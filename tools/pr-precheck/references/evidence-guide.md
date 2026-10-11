# Evidence guide: where proof lives in a PR package

Eval bundles are the complete world; use their Repo facts, Issue, Thread highlights, Plan context and Candidate PR (Title, Description, Commits, Diff, Test evidence). Never fetch the source issue. Live mode first validates scope and then reads the named local artifacts and actual issue/repository standards. An absence is a finding, not permission to invent proof.

## Plan fidelity

- **Where it lives — eval:** Plan context's accepted scope, files, approach, tests and deviations, compared with every Candidate PR Diff hunk, Commits and Description.
- **Where it lives — live:** plan.md including Deviations; issue/thread and own posted repro (or house plan/repro); the committed `git diff main...HEAD`, commit list and pr_draft.md.
- **What good looks like:** Every substantive change maps to the bounded plan or an explicit justified issue-related deviation. Folders cover their children and requested changelog entries need not have exact filenames preselected. Deferred work is stated in the plan/deviations and description. No unrelated refactor, hidden omission or false exact-adherence claim.

## Test evidence

- **Where it lives — eval:** Plan context's repro and test plan; Candidate PR Diff's fixtures; Test evidence's commands and results; Description's test claims; Repo facts' required checks.
- **Where it lives — live:** plan.md's tests, original repro output and test_evidence.md's before/after, targeted/control and repository-command output; compare pr_draft.md checkboxes and claims.
- **What good looks like:** Reproducible actions/commands paired with concrete observed results make the changed behavior checkable. Read the evidence semantically: explicit before/after observations written as prose or command annotations count, as does a named suite with a reported outcome, provided the concrete issue trigger and required controls were actually exercised. Raw stdout for every check is not mandatory unless the repo asks for it. A generic “tests pass” alone does not establish the issue's behavior; an added fixture alone proves only that it exists. Distinguish reported actual execution from proposed expectations, and reject a reproduction that exercises a different case. Record real failures, no-tests-ran outcomes and disclosed limitations without turning them into successes.

## Diff quality

- **Where it lives — eval:** Complete Candidate PR Diff and Commits, compared with Plan context, Issue and the Description's reasons for supporting changes.
- **Where it lives — live:** Entire committed branch diff and commit list, compared with plan.md/Deviations and pr_draft.md. Uncommitted fixes do not change the graded branch.
- **What good looks like:** A focused, reviewable change with relevant tests/docs, no unrelated cleanup, stray debug lines, accidental files or abandoned commented-out code. A necessary wide change has a concrete issue-related reason; no arbitrary line or commit-count threshold.

## Standards and comms

- **Where it lives — eval:** Repo facts' template and contribution/AI policy, applicable Thread highlights, Candidate PR Title/Description/checklists and test evidence.
- **Where it lives — live:** Actual PR template, docs/CONTRIBUTING.md and applicable linked policy, issue/thread, pr_draft.md and test_evidence.md. Read voice-guide.md separately for advisory personal wording notes.
- **What good looks like:** Each stated applicable repository ask is satisfied or legitimately marked N/A. Issue reference, required sections, relevant changelog/docs and required AI disclosure are concrete, not implied. No unstated policy is invented and AI use is not inferred from style. Live Path Review course disclosure belongs in Notes for Reviewers; CI remains unticked before opening. Title, description and checkboxes say only what the diff and evidence establish, including omissions and real failing checks.
