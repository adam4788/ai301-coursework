# Unit 1 — Issue Selection

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56

**Verdict output**

The following is the complete, verbatim live-mode output comparing three candidates. The selected issue is #56, ranked first and accepted.

## Evidence gathered (live, 2026-09-19)

**Repo-level facts** (apply to all three candidates):
- `codepath/pathreview-ai301-fa26-s3`: not archived, created 2026-09-10, last push 2026-09-16T21:50:20Z, no releases.
- Last 5 default-branch commits: all authored by `Aburke225` (Andrew Burke), most recent 2026-09-16T21:42:18Z — human-authored, 3 days old.
- `Aburke225` has `COLLABORATOR` author_association and posted maintainer-style close comments on issues #52 and #43 on 2026-09-16 ("Closing: ...").
- No `CONTRIBUTING.md`/`AGENTS.md`/`AI_POLICY.md` at repo root (404s). `docs/CONTRIBUTING.md` exists; full-text grep for AI/LLM/Copilot/ChatGPT/Claude terms returned nothing. `.github/PULL_REQUEST_TEMPLATE.md` and all 4 issue templates checked — no AI-disclosure checkbox anywhere.
- `gh api repos/.../pulls?state=all` returned **zero PRs** (open or closed) in the entire repo — no competing work exists for any issue right now.

**Per-issue facts:**
- **#56** "Structural chunker silently drops documents that contain no headings" — opened 2026-09-10 by Aburke225, labels `bug`,`good first issue`,`ingestion`,`tier-1`; 0 comments, 0 assignees; body has a concrete Python repro (`StructuralChunker().chunk(...)`, observed `0` vs expected non-empty), names test `test_document_with_no_headings`.
- **#57** "Tech detector counts vendored and build-output files..." — opened 2026-09-10, labels `bug`,`good first issue`,`agent`,`tier-1`; 0 comments, 0 assignees; body has a concrete repro with file list, observed `'JavaScript'` vs expected `'Python'`, names two tests (`test_node_modules_excluded`, `test_build_directory_excluded`).
- **#69** "Output parser crashes on a top-level JSON array fallback" — opened 2026-09-10, labels `bug`,`good first issue`,`rag`,`tier-1`; 0 comments, 0 assignees; body names files and an xfail manifest id (H-02) but gives no concrete input/output example or a specific named test function, only "estimated effort: 2–4 hours."

## Ranked summary (all three accepted)

1. **#56 — Structural chunker drops headingless documents.** All required checks pass; strongest fit match (document ingestion, the user's stated area of interest) plus a concrete repro and a named regression test (preferred check: pass).
2. **#57 — Tech detector counts vendored/build files.** All required checks pass; matches the "agent-tool bugs" fit interest, also has a concrete repro and two named regression tests (preferred check: pass). Ranked below #56 only because document ingestion is the closer profile match.
3. **#69 — Output parser crashes on JSON array.** All required checks pass and it matches "LLM-output handling," but the preferred reproduction/validation check is weaker — no concrete input/output example and no specific named test, only a file reference and effort estimate — so it ranks last among three otherwise-equal accepts.

No candidate was rejected; the empty comment/assignee/PR state on all three (confirmed via the repo-wide PR search returning zero results) meant the Path Review house rule for ignoring classmates' claim comments never had to be invoked — there were no claim comments to ignore.

```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "Default-branch commit by human collaborator Aburke225 on 2026-09-16T21:42:18Z, 3 days before today (2026-09-19)"},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "isArchived:false, pushedAt 2026-09-16T21:50:20Z (3 days old), well within 180-day window"},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "Single defect: StructuralChunker.chunk() returns [] for headingless docs; concrete repro script with observed=0; one named failing test test_document_with_no_headings"},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "assignees: [], comments: 0, and repo-wide `gh api .../pulls?state=all` returned zero PRs of any state"},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "docs/CONTRIBUTING.md full-text grep for AI/LLM/Copilot/Claude/ChatGPT terms returned no matches; PR/issue templates have no AI-disclosure item; no AI_POLICY.md/AGENTS.md in repo"},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "Body includes runnable Python snippet with observed output (0) and names test_document_with_no_headings"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/57",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "Same repo-level evidence: human collaborator Aburke225 commit on 2026-09-16T21:42:18Z"},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "isArchived:false, pushedAt 2026-09-16T21:50:20Z, within 180 days"},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "Single defect: tech_detector.py doesn't exclude node_modules/build paths; repro with expected 'Python' vs observed 'JavaScript'; two named failing tests"},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "assignees: [], comments: 0, repo-wide PR search returned zero PRs"},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "Same repo-level silence: no AI ban/disclosure text found in CONTRIBUTING.md, templates, or dedicated policy files"},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "Body includes runnable file-list example with observed/expected primary_language values and names two tests (test_node_modules_excluded, test_build_directory_excluded)"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/69",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "Same repo-level evidence: human collaborator Aburke225 commit on 2026-09-16T21:42:18Z"},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "isArchived:false, pushedAt 2026-09-16T21:50:20Z, within 180 days"},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "Single defect: output_parser.py calls .items() on a list and raises AttributeError; fix target stated ('fallback path should handle array responses'); references xfail manifest id H-02 and named files"},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "assignees: [], comments: 0, repo-wide PR search returned zero PRs"},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "Same repo-level silence: no AI ban/disclosure text found in CONTRIBUTING.md, templates, or dedicated policy files"},
      {"name": "Reproduction or validation starting point", "grade": "unclear", "evidence": "Body gives relevant files and an effort estimate but no input/output example and no specific named test function (only 'the covering test' referencing manifest id H-02)"}
    ],
    "verdict": "accept"
  }
]
```


---

## Eval iterations

**Run history**

1. Initial full-run attempt: `agreement: 0/0 scored items`. All 20 items errored because Claude Code's OAuth session had expired. This was an authentication failure, not 20 rubric disagreements. The harness refused to write a submission transcript. The accompanying live-mode attempt failed for the same reason.
2. Before the successful run, the ranking wording was aligned with SKILL.md: personal fit orders accepted candidates, and preferred checks support ranking or break ties. No accept/reject condition changed in that edit. After signing back into the CodePath Student 2.0 organization, a test request succeeded.
3. Complete full run with the submitted rubric: `agreement: 19/20 scored items  (bar: 18/20: PASS)`. All 20 items returned verdicts with no errors. The category line was `categories: claimed 4/4  clear-accept 7/8  dead-repo 3/3  policy 1/1  scope 4/4`. This is the unedited harness-written run committed as `eval-run.txt`. No partial eval runs or later rubric revisions were made after this successful run.

**Issue analysis**

For `issue-04` (zxcalc/zxlive#555), my rubric returned **reject**, while the gold label is **accept**. The snapshot title is "Missing several basic rule previews (#555)" and its body says, "Including remove identity, fuse spiders, remove self loops, etc."

The model's scope evidence was: "Issue lists example rules 'remove identity, fuse spiders, remove self loops, etc.' — trailing 'etc.' leaves the target set open-ended with no thread to bound it". That made the required scope check fail. Repository activity, availability, and contribution policy all passed. The preferred validation check was unclear, but preferred checks cannot cause rejection; the required scope failure caused it.

This is a false negative. The collaborator-authored issue and good-first-issue label support reading these as examples of one bounded preview task rather than an umbrella project. The model applied the concrete-target requirement too strictly to a terse report, despite the rubric saying that a short report alone does not fail. I retained the measured result rather than editing the run or adding an exception for this issue ID. It shows that explicit wording reduces ambiguity but does not eliminate model interpretation.

**Check rationale**

The complete current row for **Bounded, specified scope**, copied exactly from the uploaded `tools/issue-select/rubric.md`, is:

| Bounded, specified scope | Issue body, full available comment thread, labels, and closed-unmerged PR history; in live mode inspect referenced implementation paths where needed. | The issue requests one identifiable contribution with a concrete target behavior, documentation change, or testable defect, and no unresolved decision that prevents knowing what done means. Reject umbrella/tracking issues, pure usage questions, unresolved competing designs, and maintainer statements that the fix requires major core/parser changes. Also reject issues open for at least 2 years with at least 2 abandoned implementation PRs unless a maintainer subsequently supplies a bounded, settled approach. A short report, missing reproduction steps, an old creation date, or a multi-item checklist for one outcome does not alone fail this check. A good-first-issue label supports but does not replace scope evidence. | required |

My September 16 solo worksheet already used "Bounded, specified scope," alongside "Maintainer alive (actively merging within the month)" and "Unclaimed." The revision turns the scope label into evidence another reader can apply: look for a concrete contribution, distinguish a checklist for one outcome from an umbrella, and read maintainer comments before treating a good-first-issue label as sufficient. The age-plus-abandoned-attempts threshold is a conservative heuristic, not a course-mandated rule. Age by itself is not enough to reject.

I also separated repository maintenance from human engagement, broadened the original one-month activity window to 90 days, added an explicit AI-policy check, and kept reproduction detail preferred rather than required. These are homework revisions, not a claim that a particular group disagreement occurred. My worksheet's revision-mark section was unfinished. The 90/180/365-day cutoffs are practical defaults for a first contribution, not proof a maintainer will respond.

**Trade-offs**

The scope check trades some recall for a more predictable first task. In `issue-04`, "remove identity, fuse spiders, remove self loops, etc." was read as an unbounded target, so a gold-accepted issue was rejected. I accept that this version can miss terse but genuinely bounded maintainer requests. Conversely, accepting every maintainer-authored or good-first-issue-labeled request would let labels hide unresolved design or umbrella scope. A future revision should clarify the difference between examples within one outcome and an actual open-ended task, then re-run the full evaluation; I have not claimed such a revision was tested here.

---

## Selection rationale

**Selection rationale**

1. **Fit and time:** I selected #56 because document ingestion is directly relevant to my AI-assisted document-processing projects. Silently dropping headingless documents is a concrete correctness problem, not an open-ended feature. The issue supplies a reproduction and names `test_document_with_no_headings`, which makes it a manageable starting point for the weekly course work. I have spent about 2 hours on Unit 1 so far; that is not an estimate of how long the eventual fix will take. Environment setup and understanding chunk metadata still need to happen in Unit 2.
2. **What the verdict caught and what I weighed:** The skill correctly found a specific defect, recent human repository activity, no current assignee or competing PR, and no stated AI-contribution ban in the sources it inspected. Its accepted verdict is a screening result, not proof that the fix is trivial. I weighed the relevance to document ingestion more heavily than the other accepted candidates, #57 and #69. The important engineering outcome is preserving document text and metadata, not merely making the chunk list nonempty; the current rubric does not verify implementation quality or reproduce the bug.
3. **Claiming difficulty:** At the live check, #56 was open with no assignee, comments, or competing PR, so I expect low coordination difficulty. That can change, and I will re-check before claiming it. The section's scope rule ignores classmates' claim comments, but does not ignore assignees or active implementation PRs. I have not claimed or commented on the issue: that is Unit 2 work.

**Assistance disclosure:** AI assistance was used to develop the worksheet-based rubric, execute and inspect the evaluation/live runs, and draft this write-up. The run history and verdicts are actual tool results. No group discussion, additional personal expertise, or successful reproduction is claimed.
