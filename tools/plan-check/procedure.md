# Procedure: how this skill grades a plan package

## Read order

1. Identify live or eval mode. Read rubric.md and references/evidence-guide.md so that the required checks and evidence locations are explicit.
2. Eval: use only the supplied bundle; do not fetch or read outside sources, scope.md, or voice-guide.md. Live: read scope.md before issue-side evidence, verify the exact repo and reproduced issue, and stop if outside scope or the Repo placeholder is unfilled. Read voice-guide.md for separate outgoing-word notes.
3. Read Repo facts, Issue, and Thread highlights. Note contribution requirements, relevant maintainer directions, the original failure, and known cautions. Live equivalents are the issue and relevant repository docs identified in the guide.
4. Read Repro evidence before the candidate diagnosis. Record triggering steps, expected and actual results, and every control relevant to identifying the cause. Live: read the student's own posted reproduction; use a shipped house-repro exception only when applicable.
5. Read the entire Candidate plan, including scope, approach, tests, risks and deviations, then Candidate plan comment. Do not let the plan's confident explanation replace the observations recorded in step 4.

## Evidence gathering

Create a short evidence ledger for every rubric check, retaining deciding quotes or precise facts and their source sections:

1. Diagnosis: copy the proposed cause; pair it with the observed failure and each relevant control. Record supporting evidence and any contradiction. Identify concrete confirmation steps for a stated hypothesis.
2. Scope: collect included/excluded work and list every proposed change, including tests and docs. Compare each action with the declared issue-specific boundary; record openly deferred work rather than treating it as hidden omission.
3. Executability: collect named code locations, proposed behavior changes, work order and unresolved choices. Record any decision step that removes a blocker before implementation.
4. Test plan: pair the original failing scenario with its proposed repeatable check and stated expected-after result. List relevant controls and supplementary regression checks. Distinguish planned checks from claimed completed checks.
5. Honesty: collect concrete claims of proof/completion, admitted unknowns, material maintainer cautions, scope reductions and recorded deviations. Check each against available observations; do not add imaginary risks.
6. Comms: compare comment wording with the plan and repro; separately list each explicit thread/repo requirement and its applicable scope, plus the evidence of compliance. If no applicable requirement exists, record that absence rather than inventing one. Live personal voice breaches go in separate quoted notes.

Use the guide's live/eval locations for each gathering move. An expected section absent from a frozen bundle remains absent; do not repair it with a live lookup. In live mode, record any referenced repo facts actually inspected, but do not use unrelated private files to complete the drafts silently.

## Check execution

1. Grade all checks in table order: diagnosis-grounded, bounded-scope, executable, test-decisive, honest-claims, comment-faithful, stated-conventions.
2. For each, apply its exact pass condition to its ledger entries. Use `pass` when supported, `fail` when a needed element is clearly absent or evidence contradicts it, and `unclear` when the available text is genuinely ambiguous or insufficient to decide. An affirmative requirement with no evidence does not pass. A conditional policy requirement with no stated applicable policy is not a missing obligation.
3. Write one evidence line naming the decisive source fact or quote. Neither “looks good” nor a gold label is evidence. Re-read just the relevant passage if the ledger is insufficient; do not guess.
4. A terse plan, manual test, acknowledged uncertainty, or explicit scoped-down change can pass when the actual condition is met. Conversely, naming a cause, file or test without the required substance does not pass. Never claim the plan's expected-after output has actually occurred merely because it is written down.
5. Complete every check even after a failure. Follow the written rules without fixing them during grading; note any procedure gap before the JSON as feedback. Live voice notes are advisory unless a stated rubric condition independently fails.

## Verdict assembly

1. Apply the rubric's binary rule: all required grades `pass` gives `accept`; any required `fail` or `unclear` gives `reject`. Preferred grades never gate it.
2. Optionally summarize each check and the blockers using their actual ledger facts, including what would resolve a missing/unclear requirement. Add live voice notes separately. Do not let an overall impression override grades.
3. End with exactly the SKILL.md output schema in a fenced JSON block: `item`, all `checks` (each with `name`, `grade`, `evidence`), and `verdict`. Use the bundle id in eval mode or the exact issue URL in live mode. Valid grades are `pass`, `fail`, `unclear`; valid verdicts are `accept`, `reject`. Output nothing after that block.
