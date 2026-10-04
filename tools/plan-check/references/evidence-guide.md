# Evidence guide: where evidence lives in a plan package

In eval mode, the frozen bundle is the entire evidence set: use its Repo facts, Issue, Thread highlights, Repro evidence, Candidate plan, and Candidate plan comment. Never fetch its live source issue or consult personal voice/scope files. In live mode, first validate scope and identify the student's own posted reproduction. Grade what the draft package contains and quotes, not unrelated private notes. Missing evidence is a finding, not permission to invent facts.

## Diagnosis and grounding

- **Where it lives:** Eval: Issue's expected/actual behavior, Repro evidence's steps, outputs and controls, Thread highlights' established explanations, and the plan's cause/diagnosis. Live: scoped issue body and relevant thread, the student's own posted repro comment, and the draft's diagnosis. The submitted reproduction must be the student's proof, not a classmate's; apply the shipped house-repro exception only when applicable.
- **What good looks like:** The cause accounts for the observed failure without contradicting its controls. A mechanism still needing verification is labeled as a hypothesis and has a concrete next probe; an unsupported comment in a thread does not override measured reproduction evidence.

## Scope

- **Where it lives:** Eval: all candidate-plan scope, changes, approach and exclusions, compared with Issue and diagnosis. Live: the corresponding draft passages and any recorded deviations, read against the scoped issue and applicable house rules.
- **What good looks like:** One focused change, or an explicitly declared part of a larger issue, has an observable boundary. Supporting tests/docs may belong to that change, but unrelated cleanup or whole-subsystem rewrites do not. Read exclusions wherever expressed; do not demand specific headings.

## Executability

- **Where it lives:** Eval: candidate-plan files/functions/areas, concrete approach, ordered changes and unresolved questions. Live: those passages in the draft; use a scoped repository's referenced files or docs read-only to confirm claimed locations if needed, recording the source used.
- **What good looks like:** A stranger knows where to begin and what behavior to alter. A clearly sequenced investigation can resolve a genuine unknown before implementation; “fix it,” or “use the usual approach” without a concrete location or action cannot.

## Test plan

- **Where it lives:** Eval: Repro evidence's triggering inputs, steps, controls and failure output; compare with candidate-plan tests and their expected-after results. Live: the student's posted repro command and output, compared with the draft's planned checks and proposed success result.
- **What good looks like:** Repeating the failure-triggering steps after the change gives a stated, observable result that distinguishes success from the original failure. Manual checks are valid when decisive and repeatable. A full test-suite run is supporting regression coverage, not a substitute for the targeted result. Planned future results are not claimed as already observed.

## Honesty

- **Where it lives:** Eval: plan diagnosis, confidence language, risks, uncertainty, stated omissions and deviations; plan comment; compare with the reproduction and known maintainer warnings. Live: the same passages, the student's real reproduction and any honest deviation recorded in the draft.
- **What good looks like:** The package distinguishes what was measured, what is inferred, and what will be attempted. It acknowledges material known limitations or semantics changes, states any scope reduction, and does not present a proposed fix or unrun test as complete. No mandatory Risks heading or exhaustive speculative risk inventory is needed.

## Comms

- **Where it lives:** Eval: Candidate plan comment, compared with plan/reproduction; Thread highlights for explicit maintainer asks; Repo facts for contribution and AI-use policies. Live: the draft comment, issue thread, actual CONTRIBUTING/AI policy docs and scoped house rules. Read voice-guide.md separately in live mode and quote any personal-rule breach as a voice note.
- **What good looks like:** The comment describes the author's own issue-specific plan and respects applicable stated coordination and contribution requirements. Disclose assistance when actually required; do not infer a disclosure policy from its absence. A review-bandwidth warning is not a blanket ban. Personal voice advice alone does not change the verdict because the rubric does not make it a required check. In frozen evaluation, judge the package's stated authorship facts; do not infer how its text was produced from style.
