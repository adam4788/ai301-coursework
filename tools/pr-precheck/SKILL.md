---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

## The question

Decide whether exactly one PR package is ready to submit. Read its title, description, commits, diff and test evidence against the accepted plan, its deviations and the issue. Do not grade an issue selection or a plan instead.

## Inputs and modes

In live mode, read the named plan.md (including Deviations), pr_draft.md (title and description), and test_evidence.md. From the working copy read the complete committed branch diff using `git diff main...HEAD`, plus its commit list. Read the issue URL and relevant thread, the repository PR template and docs/CONTRIBUTING.md, including referenced applicable policies. For a house-chain student use the supplied house plan and house repro pack instead of their own plan/repro. Missing evidence remains a finding; do not invent it or run tests to silently repair the submission.

In eval mode, the supplied frozen bundle is the whole world. Use only its issue, thread, repo facts, plan context and candidate PR. Fetch nothing, read no outside evidence, and ignore scope.md and voice-guide.md. Execute every check and the complete verdict rule.

## The scope seam (live mode only)

Read scope.md before any other live evidence. If Repo is an unfilled placeholder, stop without grading and ask the student to fill the Repo line. Refuse work targeting any other repository. Apply the stated house rules; a classmate fixing the same issue does not block this student. Eval mode ignores scope entirely.

## The voice seam (live mode only)

Read voice-guide.md and compare the outgoing title and description with it. Quote broken rules in separate advisory summary notes. Voice alone does not change the verdict unless a rubric row independently requires it. Eval mode ignores this file entirely.

## Component reads

Read rubric.md for all checks and the verdict rule, references/evidence-guide.md for locations and observable proof, and execute procedure.md as written. If rubric or procedure has no authored content, refuse to grade and explain the missing component; comments and empty headings do not count. Report any procedure gap instead of improvising a replacement.

## Verdict and output

Use only accept (ready to submit) or reject (hold). Print a readable per-check summary and then the fixed schema below, populated with every rubric check in order and its deciding evidence. Use the bundle id or PR URL; before a PR exists use the supplied issue URL. End with valid fenced JSON, with nothing after it. Refusals do not masquerade as completed grades.

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

## Grading discipline

Name the deciding fact or quote for every grade. Grade the actual artifacts, not prose polish, commit count or formatting. Follow each written pass condition even when your impression differs; report rubric tensions rather than altering the check during a run. Follow the procedure and report gaps. Distinguish an added fixture from an executed test, and an assertion from printed output. Do not infer undisclosed AI use from writing style. Apply the stated treatment of unclear; if absent, unclear defaults to fail. Honest omissions and failing commands may be ready when explicitly disclosed under the rubric; silent drift or false success claims are not.
