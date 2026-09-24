# Rubric: is this reproduction package ready to post?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever
checks you define here. It ships empty on purpose: the judgment is your
work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the claim comment, the repro report's environment
     record, the artifacts read against the issue's description, the
     repo-facts block) or a location from your
     references/evidence-guide.md. "The report" is not a source; "the
     output excerpt read against the error the issue describes" is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself (does
     the artifact show the issue's behavior?), never the write-up's
     shape (how many steps it has, how long it is, whether it uses a
     template's headings). Structure-shaped checks are what make
     graders disagree with themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (ready) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. If you write no rule for
   `unclear`, the skill treats it as fail.

Cover what actually gets bad packages posted. The lecture named the
proof families: the environment is recorded, the steps are complete
and followable, the behavior shown matches the issue (not an adjacent
one), the outcome is stated honestly (an evidenced cannot-reproduce is
a pass, a confident wrong-target is not), and the words respect the
repo's conventions. A rubric that ignores a family will fail eval
packages designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Claim names the work | Claim comment read against the issue title/body and thread. | The claim identifies this issue's concrete behavior or target and says what the author will investigate or reproduce; it neither claims an unperformed result nor promises a fix already completed. A short claim is fine when specific. | required |
| Environment identifiable | Repro report's environment and code-state record read against the issue's relevant setup and repo facts. | A stranger can identify the OS/platform, relevant runtime/package versions, and repository revision or equivalent code state used, or the report explicitly explains a genuinely irrelevant field; any deviation from the issue's target setup is disclosed. | required |
| Steps followable | Repro report's starting state, essential input properties, commands/actions, and trigger read against issue reproduction context. | A stranger with the stated environment can reconstruct an equivalent input and rerun the same attempt to the observation. Exact fixture bytes are needed only when they affect the outcome; a described minimal input with enough essential properties to recreate it is sufficient. Do not require a particular count of steps or headings. | required |
| Evidence addresses this issue | Repro report's actual output/log/screenshot and input read against the issue's claimed behavior and expected outcome. | The artifact shows what happened on a relevant attempt, not merely an adjacent error or an unbacked assertion. Confirmed reproduction must show the issue's exact behavior. An honest cannot-reproduce or inconclusive attempt can pass if it shows the tested trigger and contrary result, explicitly identifies any unachieved condition, and does not claim the issue is disproved. | required |
| Outcome matches evidence | Repro report's conclusion compared with its artifact and with the issue's stated expected/observed behavior. | The conclusion accurately distinguishes confirmed reproduction, non-reproduction, and uncertainty; it makes no stronger claim than the supplied artifact supports. A documented cannot-reproduce is acceptable. | required |
| Communication respects repo | Claim and repro comment compared with issue context, repo-facts contribution/template and AI-use policy; in live mode read the repo contribution docs and issue thread. | Comments are issue-specific, do not misrepresent ownership or completed work, and follow applicable contribution or format rules. When a repo requires disclosure of ALL AI assistance in issue comments, review by this AI skill is assistance: the comment must identify the tool and extent; silence cannot verify compliance. A policy limited to PRs does not impose that rule on issue comments, and a repo with no disclosure requirement does not fail for silence. | required |

## Verdict rule

Accept if every applicable required check passes. A fail or unclear on an applicable required check means reject; preferred checks would not gate. In claim-only live mode, grade checks needing the repro report `unclear` with `not yet applicable: claim-only draft` and exclude them from the verdict. The claim and communication checks remain applicable.
