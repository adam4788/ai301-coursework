# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s3/pull/131

**Branch**

`fix/56-headingless-documents`

The PR targets `codepath/pathreview-ai301-fa26-s3:main` from my fork `adam4788/pathreview-ai301-fa26-s3`. It references `Closes #56`. Its committed diff contains only `ingestion/chunking/structural_chunker.py` and `tests/unit/test_structural_chunker.py`; local plan/comment/draft/evidence files are not in that PR.

## Eval iterations

**Run history**

The official Unit 4 harness ran against the canonical installed `~/.claude/skills/pr-precheck`, using its unchanged pinned `sonnet` model and my CodePath enterprise account.

1. First full run: **15/20**, below the bar. Categories: clear-accept 2/7, not-tested 4/4, silent-drift 4/4, standards-wall 2/2, unreviewable 3/3. The five disagreements were `pkg-05`, `pkg-08`, `pkg-11`, `pkg-13`, and `pkg-19`.
2. After revising the test-evidence rule and its claims/procedure/evidence-guide counterparts, targeted recheck: **8/8** for `pkg-08,pkg-11,pkg-13,pkg-19,pkg-07,pkg-09,pkg-12,pkg-20`. This was a partial run, not a full-course bar verdict. The last four packages were already-agreeing reject canaries across the small failure categories.
3. Confirming full run: **20/20**, PASS. Categories: clear-accept 7/7, not-tested 4/4, silent-drift 4/4, standards-wall 2/2, unreviewable 3/3. This is the last full run written by `--save-run` and committed here as `eval-run.txt`; its agreement line is `agreement: 20/20 scored items  (bar: 18/20: PASS)`.

Setup attempts before these scored runs did not yield verdicts: the work account was signed out, then the system Python could not execute the harness's Python 3.10+ type syntax. After restoring the intended CodePath enterprise login and verifying real Sonnet inference, I used the existing project Python 3.11.16. The harness/model were not modified and those setup failures are not scored runs.

**Package analysis**

`pkg-11` (ripgrep escaped trailing space): my first rubric decided **reject**, while the gold label was **accept**. It explicitly paired the reproduction with observations such as `# after: searches normally, no error` and `'foo ' not listed (ignored)`, and reported that `cargo test -p ignore` passed with 214 tests. The first rule incorrectly treated command annotations and named-suite reports as insufficient because they were not raw printed stdout. That was a representation restriction, not missing coverage of the issue. The revised rule distinguishes actual reported observations from proposed expectations; the targeted run and confirming full run both decided **accept**, matching gold.

**Check rationale**

Exact current row from `tools/pr-precheck/rubric.md`:

> | observable-tests | Test evidence against the plan's repro, targeted checks, relevant controls, and applicable repo-required commands. | The package supplies reproducible actions or commands and concrete observed results demonstrating the changed behavior, including the plan's relevant controls and applicable planned/repository checks. Actual observations may be prose, command annotations, or printed output; do not demand a raw transcript for every suite/control when its execution and outcome are explicitly reported alongside a concrete issue reproduction. A specific named command with its reported result counts; generic “tests pass” alone, expected-only results, placeholders, or testing a different case do not. A failing or unavailable check may pass when its actual outcome, reason and remaining limitation are honestly disclosed, not replaced by a success claim. | required |

I revised this row after the first full run. I rejected a requirement for a raw transcript of every suite and control: concrete before/after observations can be written as prose or command annotations, and a named test command with its reported outcome is evidence of execution. The check still requires the issue's actual trigger and the plan's relevant controls; generic “tests pass” alone and testing an easier, different case are not enough. I aligned `faithful-claims`, procedure.md and references/evidence-guide.md with that distinction rather than changing individual verdicts by hand.

**Trade-offs**

Accepting concrete narrative execution reports means the tool cannot independently authenticate every claimed suite result; raw logs would offer stronger provenance. This is a judgment tool for the supplied package, not a rerun harness for the contributed code. I kept the repro/control coverage requirement to avoid treating any specific command name as sufficient by itself.

The targeted canaries remained rejects: `pkg-07` (not-tested: only the easier single-file case, not the planned multi-file trigger), `pkg-09` (silent drift), `pkg-12` (unreviewable), and `pkg-20` (standards wall). The final full run confirms all four not-tested, all four silent-drift, all three unreviewable, and both standards-wall packages still matched gold; all seven clear accepts matched too. No new disagreement appeared in that final run.

## Verification and AI assistance

The final installed skill returned **accept** on the live PR, with all six checks pass. Its actual output is `pr-precheck-live.txt` in this folder. `CONTRACT.md` is byte-identical to the starter and the fixed SKILL JSON schema is preserved. The submitted tool files match the installed files and the four eval-loaded component fingerprints match the saved harness header.

Fresh local checks: 33 focused structural/semantic tests passed; the full unit suite reported 378 passed, 52 unrelated xfails, and 4 warnings. Ruff, mypy (76 source files), Black's non-writing check (110 files), 18 frontend tests, and the frontend production build passed. Local `make test-integration` collected zero tests and exited nonzero, explicitly disclosed in the PR as the assignment requests. Before/after reproduction: headingless chunks 0 → 1, headed control 1 → 1. Complete local output is in `test-evidence.md`.

All six GitHub check runs on exact PR head `8cac1b13463ec3dec7a4cf2016107ef19baa2ca1` passed: lint, typecheck, test-unit, test-integration, frontend, and eval. The as-opened PR description leaves CI unticked because it was opened before CI ran, as instructed; this later verification does not rewrite the as-opened evidence. No merge is claimed or required for this assignment.

I used Hermes Agent to help author and revise the skill, run the official Claude/Sonnet evaluations, inspect and test the focused fix, and draft these explanations. The scores and outputs above are actual tool results, not fabricated examples. The issue PR also discloses the AI assistance in Notes for Reviewers.
