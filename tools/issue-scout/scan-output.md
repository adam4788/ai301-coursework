## Scan results — live grading, captured 2026-10-17

**Accepted (2 of 5), in fit order:**

**1. [tbdal/Perma-Design-Kit#8](https://github.com/tbdal/Perma-Design-Kit/issues/8)** — surfaced by Q3 (`language:TypeScript label:bug`); ranking signals: title keyword "PDF" matched the relevance list, exact `bug` label, 0 comments, updated 2026-10-17T16:14:03Z. All five default-branch commits (newest `426ebb6`, 2026-10-17T09:06:21Z) are authored by human user `tbdal`; a human collaborator (`js32`, COLLABORATOR) posted a confirming reply the same day. Repo active (pushed 2026-10-17). Scope is one bounded defect (silent iOS-PWA downloads) with a proposed `saveFile()` helper, named call sites, and an explicit unit-test ask. No assignee/open PR. README's generic contributing section states no AI restriction (tree fully inspected). **Caution:** the repo is fair-source (FSL‑1.1‑MIT) — permitted for this non-commercial course use but not a fully open license. Preferred check (reproduction) passes: exact repro steps plus a confirmed workaround in the thread.

**2. [manojmallick/sigmap#973](https://github.com/manojmallick/sigmap/issues/973)** — surfaced by Q4 (`document language:JavaScript label:bug`); ranking signals: title keyword "tools" matched, exact `bug` label, 0 comments, updated 2026-10-17T15:33:57Z. Latest 5 default-branch commits are all human (`manojmallick`, most recent 2026-10-17T09:06:24Z); release v8.78.0 published 2026-10-17. Scope is one bounded docs-correctness task (fix the RepoMix comparison row, correct the MCP tool-count claim, add three sourced comparison rows, add a date/source consistency test) with explicit, testable acceptance criteria — the multi-item checklist serves one outcome, so it doesn't fail scope per the rubric. No assignee/PR. CONTRIBUTING.md and AGENTS.md were inspected; no AI-contribution ban found. Preferred check passes: concrete file paths and sourcing requirements given as the regression/validation target.

**Rejected (3 of 5):**

**3. [neomjs/neo-agent-brain#1078](https://github.com/neomjs/neo-agent-brain/issues/1078)** — Q4, title keyword "tool" matched, `bug` label exact, 0 comments, updated 2026-10-17T16:11:53Z. **Deciding failure: maintainer engagement.** The repo's own README (lines 78–85) names its committers/reviewers as AI personas ("Mnemosyne… AI maintainer", "Euclid… AI maintainer", etc.); the latest 5 default-branch commits were all merged PRs authored and reviewed exclusively by these bot identities (e.g. PR #1065 reviewed only by `neo-opus-grace`, merged 2026-10-16T15:31:19Z), and the 5-issue maintainer-response sample returned no human reply. Per-instruction, bot/AI-persona activity does not establish human engagement. Scope is also doubtful (a dense internal "Institution"/Fleet-lifecycle ticket written for the project's own AI team, not a newcomer-legible task), but engagement alone already sinks it.

**4. [0xMaxMa/claude-gateway#615](https://github.com/0xMaxMa/claude-gateway/issues/615)** — Q3, no title keyword match (camelCase `agentDeclaration` doesn't count as whole-word "agent"), exact `bug` label, 0 comments, updated 2026-10-17T15:54:49Z. Maintainer engagement, repo health, scope, and AI policy all pass (human commits same day, release v2.1.2 on 2026-10-17, precisely-specified bug with line numbers and a named regression test, silent on AI use). **Deciding failure: unclaimed/no competing work.** PR [#617](https://github.com/0xMaxMa/claude-gateway/pull/617) is open, linked via GitHub's Development panel to #615, and was opened 2026-10-17T16:11:26Z by the same author — an open implementation PR already exists for this issue, which fails the required check regardless of who authored it.

**5. [anthropics/claude-code#103018](https://github.com/anthropics/claude-code/issues/103018)** — Q3, title keyword "tools" matched, exact `bug` label, 0 comments, updated 2026-10-17T15:17:30Z. **Deciding failure: maintainer engagement.** The 5 most recent default-branch commits are all `chore: Update CHANGELOG.md…` / `Update mods/` commits authored by "GitHub Actions"/`actions-user` (newest 2026-10-16T20:52:45Z), with no human-authored or human-reviewed commit in the sample and no PR evidence attached to any of them; the 5-issue maintainer-response sample shows no human reply on any thread. Scope is also weak: the issue is largely an investigative billing-metering report ending in an open policy question ("Is it intended that…?"), not a single bounded, settled task.

```json
[
  {
    "item": "https://github.com/tbdal/Perma-Design-Kit/issues/8",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "Latest 5 default-branch commits all authored by human user tbdal, newest 426ebb6 at 2026-10-17T09:06:21Z; COLLABORATOR js32 replied in-thread the same day the issue opened (2026-10-17T16:24:09Z)."},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "Not archived; repo pushed_at 2026-10-17T09:06:23Z, well within 180 days (no release required once commit condition is met)."},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "Issue proposes one concrete fix (saveFile() helper for installed-PWA downloads) naming exact call sites and a unit-test criterion; not an umbrella issue or open design debate."},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "development.assignees=[] and closedByPullRequestsReferences=[] as of capture 2026-10-17T16:45:19Z; the sole comment is a root-cause confirmation, not a claim."},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "Full repo tree inspected (treeReceiptSha256 db84260…); README.md Contributing section (fetched 2026-10-17) states only fork/branch/PR steps with no AI restriction; no AI_POLICY/AGENTS ban file present."},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "Body gives exact repro steps (Settings → Backup herunterladen (JSON)) plus a confirmed working workaround (navigator.share) from the 2026-10-17T16:24:09Z comment."}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/manojmallick/sigmap/issues/973",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "Latest 5 default-branch commits all authored by human user manojmallick, newest c7d9903 at 2026-10-17T09:06:24Z."},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "Not archived; release v8.78.0 published 2026-10-17T09:07:23Z (within 365 days)."},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "Issue targets one outcome (sourced, dated comparison-page claims) via a single acceptance-criteria checklist naming exact files (docs-vp/guide/compare-alternatives.md, README); multi-item checklist for one outcome does not fail scope per rubric."},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "development.assignees=[] and closedByPullRequestsReferences=[] as of capture; 0 comments, opened and labeled by OWNER manojmallick on 2026-10-17T10:26:35Z."},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "CONTRIBUTING.md and AGENTS.md fetched and inspected (sha c34d596…, 6b4fc26…); neither states a ban on AI-generated contributions."},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "Acceptance criteria name exact doc rows to correct and require 'A test pins the date-and-source rule'."}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/neomjs/neo-agent-brain/issues/1078",
    "checks": [
      {"name": "Maintainer engagement", "grade": "fail", "evidence": "README.md (lines 78-85, fetched 2026-10-17) names commit/review identities as AI personas (e.g. neo-opus-grace = 'Grace, AI maintainer'); PR #1065 merged 2026-10-16T15:31:19Z was authored and reviewed only by neo-gemini-pro/neo-opus-grace; the 5-issue maintainerResponseSample (incl. #1077, #144) shows firstMaintainerReply:null for every sampled thread."},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "Not archived; default branch (dev) pushed 2026-10-17T01:51:24Z, within 180 days."},
      {"name": "Bounded, specified scope", "grade": "unclear", "evidence": "Body is an internal 'Institution/Fleet lifecycle' continuity ticket requiring cross-reference to prior ADRs, Decision Records and sibling tickets (#1074, #674, #964) with no single settled design named as final."},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "development.assignees=[] and closedByPullRequestsReferences=[] as of capture 2026-10-17T16:45:19Z; 0 comments on the issue."},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "Full tree inspected (treeReceiptSha256 e301fee…); README mentions only 'cross-family review before merge', no ban on AI-assisted work."},
      {"name": "Reproduction or validation starting point", "grade": "unclear", "evidence": "Acceptance criteria (AC-1…AC-4) describe internal unit-test shapes for files only this project's own agents have working context on; no external-reproducible repro given."}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/0xMaxMa/claude-gateway/issues/615",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "Latest 5 default-branch commits authored by human user 0xMaxMa, newest c6e867b at 2026-10-17T08:00:07Z."},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "Not archived; release v2.1.2 published 2026-10-17T08:05:38Z."},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "Body pinpoints exact lines (installer.ts:2471-2482, :2537) and a required regression test in tests/unit/apps/installer.test.ts."},
      {"name": "Unclaimed / no competing work", "grade": "fail", "evidence": "development.closedByPullRequestsReferences lists PR #617 (state OPEN, merged_at null), created 2026-10-17T16:11:26Z, explicitly 'Closes #615' — an open implementation PR already exists."},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "website/reference/development.md fetched (sha 5ef622d…) has no AI-contribution restriction; no dedicated AI policy file found in the inspected tree."},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "AC specifies exact reconfigure() regression test steps (toggle disable_archive, assert registry.get(appName).agentDeclaration)."}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/anthropics/claude-code/issues/103018",
    "checks": [
      {"name": "Maintainer engagement", "grade": "fail", "evidence": "Latest 5 default-branch commits (newest c017428c, 2026-10-16T20:52:45Z) are all 'chore: Update CHANGELOG.md and feed.xml' / 'Update mods/' commits authored by GitHub Actions/actions-user with no attached PR (automatedCommitPRReviewEvidence returns [] for all 5); maintainerResponseSample across 5 issues (incl. #28300, #102142) shows firstMaintainerReply:null for every thread."},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "Not archived; release v2.1.302 published 2026-10-16T20:53:06Z."},
      {"name": "Bounded, specified scope", "grade": "fail", "evidence": "Body ends in an open policy question ('Is it intended that requests... count against plan limits? If yes... if no, this looks like a bug') rather than one settled, testable target behavior."},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "development.assignees=[] and closedByPullRequestsReferences=[] as of capture 2026-10-17T16:45:19Z."},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "Full tree inspected (treeReceiptSha256 9c6138d…); README.md (fetched 2026-10-17) states a data/privacy policy but no ban on AI-assisted contributions."},
      {"name": "Reproduction or validation starting point", "grade": "unclear", "evidence": "Methodology relies on the reporter's own private ~/.claude/projects transcripts and undisclosed internal metering code, not reproducible by an external contributor from the public repo alone."}
    ],
    "verdict": "reject"
  }
]
```

---

## Issue-scout: direct grading — Unit 5, 2026‑10‑17

**Mode:** live, direct (3 hand-fed URLs, no search/ranking). Rubric and evidence read fresh from `/Users/adamnugroho/.claude/skills/issue-scout/{SKILL.md,scope.md,rubric.md,references/evidence-guide.md}`. Evidence from `.hermes/unit-5/homework/direct-evidence/` raw JSON only (`development-links.json`, `assessment.json`, and the gathering agent's `README.md` were not used).

### Accepted

**1. Logixia/logixia#120 — `fix(browser): child() loses the json option and strips the wrong key`** — accept
- Repo active and maintained: human-authored, signed commits as recent as 2026-10-09 (`webcoderspeed`, PGP-verified), not archived, release `v1.12.5` published 2026-10-09.
- Opened by a `COLLABORATOR` (the repo's dominant committer) with an exact file/line reference (`src/browser.ts` line 391), a verified before/after observation (`parent console transport has json: true, child has json: false`), a named test file (`src/__tests__/browser.test.ts`), specific tests to add, and concrete acceptance criteria (`npx jest ...`, typecheck, lint).
- The "Decide on context" bullet reads as unresolved at a glance, but the same sentence already names the resolution ("keeping it in the payload... is the least surprising. Remove the `_` destructure and fix the comment") — not an open design debate, so scope stays bounded.
- No assignees, no comments at all, `closedByPullRequestsReferences` empty, PR search 0 hits, and the complete 16-entry open-PR list contains nothing touching `browser.ts`/`child()`/#120 — genuinely unclaimed.
- No AI-contribution ban in `CONTRIBUTING.md`, the PR template, or `CODE_OF_CONDUCT.md`; silence after checking all three passes.
- Fits the profile well: bounded TypeScript bug fix with an explicit observable result and a defined regression-test path.

### Rejected

**2. Nano-Collective/nanocoder#1631 — `[Bug] XML tool call after a code fence is ignored`** — reject
- Passes maintainer engagement, repo health (human-signed commit today, release `v1.31.0` 2026-09-26), bounded scope (single parser function, explicit reproduction, expected vs. actual), and AI-assisted-contributions permitted (no ban in `CONTRIBUTING.md`/`AGENTS.md`/`CLAUDE.md`/PR template — those files are agent instructions, not a ban).
- **Fails Unclaimed/no competing work**: `ducanhnguyen223` posted a detailed claim-with-plan comment on 2026-10-08 ("I'd like to take this... I'll keep this scoped to markdown-fence handling..."), 9 days before this scan — well inside the rubric's 90-day staleness window, and never withdrawn. The only maintainer-adjacent reply told them not to open a PR *without* being assigned first, which is a procedural hold, not a withdrawal or an invitation for new takers. `gh issue view` confirms no assignee and no closing PR, but the comment-only claim itself is still active per the rubric's literal pass condition.

**3. Nano-Collective/nanocoder#1633 — `[Bug] Default compaction treats any mention of success as the whole tool result`** — reject
- Passes maintainer engagement, repo health, bounded scope, and AI-assisted-contributions permitted (same repo-level evidence as #1631).
- **Fails Unclaimed/no competing work** on two independent grounds: `gh issue view` shows a current assignee (`Vishesh-Verma-07`, assigned 2026-10-16) **and** `closedByPullRequestsReferences` lists an open PR, #1645 (`qwist1233-cpu`, opened 2026-10-08, confirmed `state: open`, `merged_at: null` in `pulls/1645/pull.json`, body text "Closes #1633"). The PR's own stated test results (31 AVA tests passing, negative check, `biome`/`tsc` clean) are the author's claims in the PR body — not verified by this scan.

---

```json
[
  {
    "item": "https://github.com/Logixia/logixia/issues/120",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "commits.json: human-authored, PGP-verified commit by webcoderspeed on 2026-10-09 (8 days before scan date 2026-10-17)"},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "repository.json archived:false; latest-release.json shows v1.12.5 published 2026-10-09 (within 365 days)"},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "issue.json body: exact file/line (src/browser.ts:391), verified before/after behavior, named test file src/__tests__/browser.test.ts, and acceptance criteria (npx jest ..., typecheck, lint); the 'decide on context' bullet names its own resolution in the same sentence"},
      {"name": "Unclaimed / no competing work", "grade": "pass", "evidence": "issue.json: assignees:[], comments:0; development-gh-view.json: closedByPullRequestsReferences:[]; pr-search.json: total_count 0; open-pulls.json (16 entries) contains no PR referencing browser.ts/child()/#120"},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "policy-files/CONTRIBUTING.md, .github/pull_request_template.md, and CODE_OF_CONDUCT.md contain no AI-contribution ban or restriction"},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "issue.json body: 'Verified: parent console transport has json: true, child has json: false' plus named test command npx jest src/__tests__/browser.test.ts"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/Nano-Collective/nanocoder/issues/1631",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "commits.json: human-signed commit by yetuge merging PR #1421 on 2026-10-17 (scan date)"},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "repository.json archived:false; latest-release.json v1.31.0 published 2026-09-26 (within 365 days)"},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "issue.json body: single function (XMLToolCallParser.parseToolCalls), explicit repro steps, expected vs actual behavior"},
      {"name": "Unclaimed / no competing work", "grade": "fail", "evidence": "comments.json: ducanhnguyen223 posted a detailed claim-with-plan on 2026-10-08 ('I'd like to take this...'), 9 days before scan date, never withdrawn; only reply was a procedural hold ('don't raise PR without getting the issue assigned'), not a withdrawal or new-taker invitation"},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "policy-files/CONTRIBUTING.md and pull_request_template.md contain no AI ban; AGENTS.md/CLAUDE.md are agent-instruction files, not restrictions"},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "issue.json body gives a minimal fenced-code-then-tool-call repro and exact expected/actual output"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/Nano-Collective/nanocoder/issues/1633",
    "checks": [
      {"name": "Maintainer engagement", "grade": "pass", "evidence": "commits.json: human-signed commit by yetuge merging PR #1421 on 2026-10-17 (scan date)"},
      {"name": "Repository still maintained", "grade": "pass", "evidence": "repository.json archived:false; latest-release.json v1.31.0 published 2026-09-26 (within 365 days)"},
      {"name": "Bounded, specified scope", "grade": "pass", "evidence": "issue.json body: single function (compressToolResultDefault/isSuccess), explicit repro steps, concrete expected vs actual output"},
      {"name": "Unclaimed / no competing work", "grade": "fail", "evidence": "development-gh-view.json: gh issue view shows assignee Vishesh-Verma-07 (assigned 2026-10-16) AND closedByPullRequestsReferences lists PR #1645; pulls/1645/pull.json confirms state:open, merged_at:null, body 'Closes #1633'"},
      {"name": "AI-assisted contributions permitted", "grade": "pass", "evidence": "policy-files/CONTRIBUTING.md and pull_request_template.md contain no AI ban; AGENTS.md/CLAUDE.md are agent-instruction files, not restrictions"},
      {"name": "Reproduction or validation starting point", "grade": "pass", "evidence": "issue.json body gives exact repro conditions (multi-line log with 'completed successfully' and a failure line) and the exact wrong output produced"}
    ],
    "verdict": "reject"
  }
]
```
