# Contribution: Service icons and required-icon validation

Path: `beat-2-contribution/contribution-story.md`

This file is Assignment 5, and it is graded at the path above; a copy kept anywhere else in
the repository is not read. **Keep every section header below under its exact name** — the
format criteria grade exactly that. Your course repo link is the whole submission: no tool
files and no evidence uploads are part of Assignment 5.

**Contribution Number:** [1]
**Student:** Adam Nugroho
**GitHub Username:** adam4788
**Issue:** https://github.com/betterlaspinas/betterlaspinas/issues/274
**Pull Request:** Not opened; maintainer assignment/approval is pending.

**Preparation status (November 10, 2026):** Partial contribution story, updated with AI assistance from existing work and verified source evidence. No completed fix, PR, or portal submission is claimed. The issue remains open and unassigned; its two comments are my claim and follow-up, with no maintainer response or thumbs-up. The technical plan below is proposed work, not implementation.

One repository, built across units 5 to 8, telling the whole story of your real
contribution. Fill it as you work, not at the end — the sections below ask for evidence that
is far easier to write down as it happens than to reconstruct in the last weekend.

Contribution Number stays `[1]` unless you make more than one contribution this term; it
just numbers them.

---

## Toolkit

Every story section below, from Why I Chose This Issue through Pull
Request, ends with a Toolkit block: which tool did that phase's work
and how you used it, what it produced, what difficulties or
shortcomings it presented, and what you changed or would change
because of them. Together the blocks are the thread the rubric's
Toolkit points read, and they are the raw material for your unit-9
portfolio, so keep them current as you work rather than
reconstructing them later.

A Toolkit block looks like this (copy it into each story section and
fill it there):

```text
**Toolkit**

- Tool: [which tool did this phase's work, and how you used it]
- What it produced: [described in a sentence or a short excerpt]
- Difficulties: [what fought you or fell short, or "none met"]
- What changed: [the patch, revision, or workaround, what you would
  update, or "nothing"]
```

This section also keeps one short dated entry per week of tool work,
starting below: what you built or changed that week, what broke, and
what you changed because of it. The blocks tell the story where it
happened; these entries are the toolkit's own timeline.

All four entries are graded. Keep every heading below, and fill each
one in the week it belongs to.

**Unit 5: issue-scout migration, reproducible search, and live candidate grading**

2026-10-17 — Migrated the Unit 1 skill to `issue-scout`, preserving the complete backup, rubric, evidence guide, and original fit-profile paragraph, then authored four TypeScript/JavaScript queries grounded in the documented web/document project history and tested deterministic URL dedupe and metadata-only ranking. The executed queries returned 400 records, 396 unique issues, and 295 survivors; real CodePath-work Claude grading of the exact top five produced two accepts and three rejects, with the complete read-out saved in [scan-output.md](../tools/issue-scout/scan-output.md). A separate direct run on three issues from the course Issue Selection site accepted [Logixia #120](https://github.com/Logixia/logixia/issues/120), rejected [nanocoder #1631](https://github.com/Nano-Collective/nanocoder/issues/1631) for a recent unwithdrawn claim, and rejected [nanocoder #1633](https://github.com/Nano-Collective/nanocoder/issues/1633) for an assignee and open PR; these are graded candidates, not a final issue choice or claim. The work OAuth session had expired and the first tool-driven scan hit its budget guard, so the work subscription was restored and tested before grading, the failed attempt was retained, and the same top five were completed using compact source-hashed live evidence; the actual failures, fixes, and the broad ranking's specialist/closed-source false leads are recorded in [dated scan notes](../tools/issue-scout/scan-notes.md).

**Unit 6: voice guard, shared repo memory, fresh grading, and initial reproduction**

2026-10-21 — Installed the staff voice guard, preserved all prior rules in one shared guide, updated the real-repository scopes, and verified clean-draft PASS, unsupported-result STOP, and actual Claude Code hook blocking; the Upstream examples are AI-assisted drafts. Fresh scouting rejected three occupied Logixia candidates and accepted two replacement site picks, after which I explicitly chose [Better Las Piñas #274](https://github.com/betterlaspinas/betterlaspinas/issues/274), reserved it on the course site, and approved the [posted claim/request for assignment](https://github.com/betterlaspinas/betterlaspinas/issues/274#issuecomment-6330461055). A broad troubleshooting rule initially blocked a legitimate scope question, so the guide was clarified to distinguish troubleshooting from assignment/scope requests while still blocking invented test results; stale candidates, an overstrict local JSON validator, and two unsuccessful Claude posting attempts were preserved rather than presented as successes. One scoped orientation was distilled into a locally excluded `CLAUDE.local.md`, the unmodified checkout produced [initial data/schema evidence](reproduction/README.md) with one positive control passing and three contract assertions failing, and a [browser/baseline follow-up](reproduction/visual/README.md) confirmed eight empty-icon headings with an 8 px gap while lint, typecheck, build, and all 299 baseline tests passed under the recorded environment; maintainer approval remains pending.

**Unit 7: ship-gate installation and baseline checks**

2026-11-04 — Installed the public starter's ship-gate and a local, CI-sourced manifest with validation, lint, typecheck, and a single test run; all four checks passed on the unmodified `main` checkout, not on an implementation branch. A new Claude Code session dispatched both the voice guard and ship-gate, and both blocked the `gh pr create --help` test; separate synthetic tests also blocked a direct PR attempt on `main`. The test run rewrote tracked `.nuxtrc` from test-utils 4.1.0 to the installed 4.2.0, so I restored its exact pre-run contents; the starter hook also failed to detect a nested-shell test, so it is not a universal safeguard. The live Unit 7 Assignment instructions remain unread, and no full gate pass, fix, or PR is claimed; maintainer approval is still pending.

**Unit 8: [one line on the tool work]**

[2-4 sentences: the PR-monitor and your playbook. What it read, what it
drafted, what you did with the draft.]

---

## Why I Chose This Issue

**The factual account below was drafted with AI assistance.**

On October 21 I selected Better Las Piñas #274 after reviewing the recommendation and explicitly approving its reservation and exact claim wording. Last week's accepted Logixia #120 was no longer resolvable, and fresh thread/PR checks rejected Logixia #31, #30, and #35 as occupied; I did not claim over those contributors. The patched scout accepted #274 and Kaoto #3527. #274 has a concrete TypeScript/JSON data-and-validation target with a runnable regression starting point, consistent with the documented fit profile; the Kaoto alternative had a less certain Monaco diagnosis. The full replacement read-out is saved in [unit6-replacement-regrading.md](../tools/issue-scout/unit6-replacement-regrading.md).

The scout helped by reading occupancy beyond assignees: Logixia #30 had no comments or assignee but already had a partial open implementation PR. It is not a substitute for fresh source checks: the chosen issue describes 50 services and 44 missing icons, while the tested revision has 45 and 39, and its home page uses a separate static icon list. Its summary called #274 moderate despite flagging an open validation edge; under the supplied difficulty definition that edge warrants an ambitious caution until clarified, without changing the accept verdict. My [claim/request for assignment](https://github.com/betterlaspinas/betterlaspinas/issues/274#issuecomment-6330461055) is posted and verified as `adam4788`; I am waiting for maintainer approval before implementation.

The project interests me because it is connected to a city, which makes it easier for me to visualize who I am helping and who the work could impact.

On October 28, I reviewed and approved the summarized communication rules; the examples remain labeled as AI-assisted and hypothetical.

I want to learn what kinds of imagery or icons balance professionalism, accessibility, and creativity.

**Toolkit**

- Tool: `issue-scout` in direct live mode using source-hashed evidence from current course-site candidates and actual Claude-work Sonnet grading.
- What it produced: three Logixia rejects, then two replacement accepts; Adam selected #274 and approved its verified public claim.
- Difficulties: stale issue URLs, competing PRs without assignees, and a difficulty-summary edge the raw grader understated.
- What changed: replaced strict scope rejection with `scope-feasible`, added separate live difficulty notes, and retained explicit reviewer cautions instead of silently editing raw model output.

---

## Understanding the Issue

**Problem Description**

AI-assisted factual draft: service records can omit icons, leaving an unconditional icon slot in the category-card heading, while schema/type validation does not require the field.

**Expected Behavior**

Every canonical service should have a meaningful, non-empty Bootstrap icon; omission should fail validation and the type should require the field. Category-card alignment and the home-page spot checks must be verified in a running app.

**Current Behavior**

At tested upstream revision `7fffa3961785b1b04dd27252650c4c811d22ad5a`, 39 of 45 services omit `icon`; the baseline config check still passes, and the real validator accepts both omitted and empty icon values. The production-built browser page now confirms all eight Business card headings have zero-width icons but an 8 px gap; the six Certificates cards provide real-glyph controls, with screenshots and DOM geometry saved in the [follow-up report](reproduction/visual/README.md).

**Affected Components**

`app/config/services.json`, `app/config/schema/services.schema.json`, `app/types/config.ts` (`ServiceItem`), `scripts/validate-config.mjs`, and `app/pages/services/[category].vue`. The home `PopularServices.vue` component was inspected and currently uses a separate static icon list.

**Toolkit**

- Tool: one scoped Claude-work orientation over the catalog, schema, type, category/home entrypoints, and validator; direct source inspection verified the summary.
- What it produced: local `CLAUDE.local.md` with the maintainer's AGENTS import, relevant commands, claim/approval status, and distilled subsystem findings; `git check-ignore` verifies the memory stays local.
- Difficulties: the model inferred maintainer intent from an optional field and lacked the home component's internals; neither inference was accepted as proof.
- What changed: inspected `PopularServices.vue` directly, recorded its separate static data source, and retained the exact catalog-count discrepancy.

---

## Reproduction Process

**Environment Setup**

macOS 27.0.1 ARM64, Node v26.7.0, project 1.2.0 at unmodified upstream `7fffa3961785b1b04dd27252650c4c811d22ad5a`. Initially pnpm was absent and only the dependency-free actual validator was run; subsequently pinned pnpm 10.29.2 installed the frozen lockfile through a registry mirror after the normal registry timed out. Tests require `TZ=UTC` and `NODE_OPTIONS=--no-experimental-webstorage` on this host; the production build also uses `NUXT_SITE_URL=https://betterlaspinas.org` from `.env.example`. Full commands, failed controls, actual baseline results, screenshots, and limits are in [the browser follow-up](reproduction/visual/README.md); [the initial report](reproduction/README.md) is preserved as history.

**Steps to Reproduce**

1. Clone upstream separately and check out `7fffa3961785b1b04dd27252650c4c811d22ad5a`; leave its source unchanged.
2. Run `node scripts/validate-config.mjs` from that checkout: actual exit 0 despite missing catalog icons.
3. Set `ICON_REPRO_REPO` to that checkout and run the coursework [icon-contract.test.mjs](reproduction/icon-contract.test.mjs) using `node --test`: actual exit 1, one positive control passes and three desired-contract assertions fail.
4. Preserve that first run as partial data/schema reproduction, not a fixed issue.
5. Install the frozen dependencies, run the existing baseline scripts with the recorded host environment, build production, then inspect Business and Certificates pages in a local Chrome session at 1280, 390, and 320 px as documented in [the follow-up](reproduction/visual/README.md).
6. Record real icon glyphs, zero-width missing icons, computed gap, and title offsets without DOM changes; stop the server after screenshots/measurements. Baseline suite success is not a fix for the still-RED issue contract.

**Reproduction Evidence**

- **Commit showing reproduction:** no implementation fork/commit yet; maintainer approval is pending. Exact [upstream revision tested](https://github.com/betterlaspinas/betterlaspinas/commit/7fffa3961785b1b04dd27252650c4c811d22ad5a); reproduction artifacts are kept in this course repo.
- **Screenshots/logs:** [initial RED output](reproduction/initial-red-output.txt), [runnable harness](reproduction/icon-contract.test.mjs), [Business desktop](reproduction/visual/business-desktop.png), [Certificates control](reproduction/visual/certificates-desktop.png), [mobile](reproduction/visual/business-mobile.png), [narrow](reproduction/visual/business-narrow.png), [DOM measurements](reproduction/visual/layout-metrics.json), and [actual baseline receipts](reproduction/visual/baseline-results.json).
- **My findings:** confirmed missing data, non-enforcement of the icon contract, and the rendered 8 px leading gap beside empty Business icons; the 8 Business titles are consistently indented rather than randomly misaligned with one another. Actual catalog counts and the home page's separate static icon list differ from the issue's description; these remain clarification points. An unrelated narrow-screen header overlap is documented but not changed.

**Toolkit**

- Tool: the actual upstream Node validator, a separate Node contract harness, and live `repro-check` grading through Claude-work Sonnet.
- What it produced: intentional issue RED (1 positive control pass / 3 contract failures), [initial repro-check accept with six checks](reproduction/repro-check-output.md), production browser screenshots/geometry, and a separately passing baseline (299 tests across 18 files, lint, typecheck, validation, build).
- Difficulties: initial package-registry timeout, absent pnpm, Node 26 web-storage interference, timezone-dependent dates, a missing build site URL, and ESLint including the private local notes despite Git exclusion; source counts/home data wiring also differ from the issue.
- What changed: used the pinned package-manager mirror without changing the lockfile, formatted only private notes, isolated Node storage and UTC as controls, supplied the documented site URL, and preserved first failures alongside passing receipts. No upstream code/assertions were weakened; passing baseline is not an issue fix, and maintainer approval is still required.

---

## Solution Approach

**Analysis**

AI-assisted analysis of the recorded, unmodified revision `7fffa3961785b1b04dd27252650c4c811d22ad5a`: `app/config/services.json` has 39 of 45 services without icons. `definitions.service.required` in `app/config/schema/services.schema.json` omits `icon`, and `ServiceItem` in `app/types/config.ts` makes it optional. The category-card template in `app/pages/services/[category].vue` renders the empty icon element inside a heading with a gap. In `scripts/validate-config.mjs`, `validateNode` checks required properties and types, but has no string-length or pattern validation; adding a schema constraint alone would therefore not enforce a non-empty value in this validator.

**Proposed Solution**

After maintainer assignment or approval, recheck current main and its contribution instructions, then backfill meaningful Bootstrap icons before requiring the field. Keep the change focused on the service catalog and its icon contract. Preserve existing valid icon choices, unrelated service content, routes, and the home page's separate static list. Clarify the whitespace-only edge with the maintainer before claiming that behavior is agreed. No code implementing this proposal has been written.

**Implementation Plan**

1. Recheck issue #274, its assignment, current main, and service counts. The recorded 45/39 counts are from the pinned reproduction, not a claim about today's upstream main.
2. Update missing `icon` values in `app/config/services.json` using per-service Bootstrap classes consistent with `categories.json` and existing certificates. Run configuration validation before changing the contract.
3. Add `icon` to `definitions.service.required` in `app/config/schema/services.schema.json`, declare `ServiceItem.icon` required in `app/types/config.ts`, and implement an explicitly agreed non-empty string rule in `scripts/validate-config.mjs` / `validateNode`. Add regression checks through `validateAgainstSchema` so requiredness and non-empty enforcement are actually exercised.
4. Re-run the issue reproduction against the changed checkout, inspect category pages and the home page, and run validation, lint, typecheck, tests, and build. Record any runtime controls and actual outputs.
5. Review the complete diff, record any deviations, run the installed ship-gate on the real contribution branch, and prepare the PR with before/after evidence and AI-use disclosure. No PR opening or push is part of this preparation.

**Deviations:** Implementation has not started. There are no implemented deviations to report.

**Toolkit**

- Tool: direct inspection of the pinned source and existing reproduction harness; AI-assisted plan drafting.
- What it produced: a file- and function-specific proposed plan, including the validator's missing string-constraint handling.
- Difficulties: maintainer approval is absent, the recorded catalog counts differ from the issue, and whitespace behavior is unresolved.
- What changed: separated proposed work from completed work and made validator coverage an explicit step instead of assuming schema metadata is enforced.

---

## Testing Strategy

The first observable check is the issue-specific reproduction before and after the future fix. Re-run `reproduction/icon-contract.test.mjs` against the chosen implementation checkout: the real validator must accept a valid icon, reject a missing icon, reject an empty icon, and the full catalog must have nonblank values. The saved baseline is one pass and three intentional failures; no after-fix result exists yet. Add a whitespace-only case if that requirement is agreed.

For the visual part, repeat the recorded Business/Certificates comparison at 1280, 390, and 320 px. Verify actual icon glyphs and title geometry, then check the other categories and home Popular Services. The existing screenshots demonstrate the baseline, not the proposed result.

The second observable check is the project's own validation and suite: `pnpm validate`, `pnpm lint`, `pnpm typecheck`, `pnpm test --run`, and `pnpm build`. Capture actual output for the implementation revision and report failed or unrun checks explicitly. The previous 299-test baseline and November 4 manifest checks are historical results on unmodified main. The real branch must pass the full ship-gate and pr-precheck; a hook wiring test does not satisfy that requirement.

**Toolkit**

- Tool: the existing Node contract harness, production-browser evidence, and the installed ship-gate manifest.
- What it produced: a concrete before/after test plan anchored to saved failing contract tests and passing baseline controls.
- Difficulties: Node 26 storage and timezone behavior required documented environment controls; the gate's nested-shell detection has a known gap.
- What changed: require the issue-specific contract and visual checks alongside the normal suite, and distinguish all historical baseline results from future implementation results.

---

## Implementation Notes

**2026-10-21:** Completed initial data/schema reproduction and later production-browser checks on unmodified upstream. The contract was intentionally RED while the normal baseline passed; no fix was made. See [initial evidence](reproduction/README.md) and [browser follow-up](reproduction/visual/README.md).

**2026-10-28:** Posted the approved [follow-up](https://github.com/betterlaspinas/betterlaspinas/issues/274#issuecomment-6484502126) asking whether the issue was available and reporting the actual catalog-count discrepancy. No assignment was inferred from posting it.

**2026-11-04:** Installed the public-starter ship-gate and tested its four manifest checks on unmodified main. Both installed hooks blocked a direct PR help test, while a synthetic nested-shell test exposed a detection gap. The test-induced `.nuxtrc` change was restored to its exact prior content. No implementation branch, PR, or full gate pass resulted.

**2026-11-10:** Checked the existing Hermes course history and local files before duplicating work. The latest course session had explicitly reported the story and submission incomplete. Rechecked the live issue and both comment reaction lists: open, unassigned, two comments by `adam4788`, no maintainer response or reaction. Prepared the technical plan and testing strategy above, with AI assistance, while preserving the hold on implementation.

**Toolkit**

- Tool: Git status/history, existing Hermes course records, source inspection, and live GitHub issue/comment/reaction reads.
- What it produced: an evidence-grounded dated log and a clear distinction between installed tooling, proposed implementation, and completed contribution work.
- Difficulties: the previous standalone safe-draft file was no longer present, and local Unit 7 edits had not been pushed.
- What changed: recovered the actual progress from the canonical story and saved receipts rather than claiming that prior activity practice completed Assignment 5.

---

## Pull Request

**PR Link:** Not opened.

**PR Description:** Not published. A future description must identify issue #274, the exact implemented scope, before/after contract and visual results, normal check results, and AI assistance. These results must be recorded after the work actually occurs.

**Maintainer Feedback:**

- 2026-11-10: No maintainer response or reaction appears on the claim or follow-up. The issue has no assignee. The contribution instructions require assignment or a maintainer thumbs-up before starting.
- No feedback has been addressed because none has been received.

**Status:** Not opened; awaiting maintainer assignment or approval before implementation. A local draft and passing baseline are not a submitted PR.

**Toolkit**

- Tool: live GitHub issue, comment, and comment-reaction reads.
- What it produced: verified current claim status and confirmed no maintainer thumbs-up on either of my comments.
- Difficulties: the project has not responded to the claim or follow-up.
- What changed: retained an explicit blocked status instead of filling a nonexistent PR URL or claiming a full gate pass.

---

## Learnings and Reflections

**Technical Skills Gained**

Pending Adam's own reflection. Evidence available to discuss includes the gap between schema metadata and the actual validator, the distinction between issue-contract failures and a green baseline, and hook wiring versus a full branch gate pass. These prompts are AI-assisted and are not presented as personal reflections already supplied by Adam.

**Challenges Overcome**

The factual work record includes a package-registry timeout handled with the pinned package-manager mirror, Node storage/timezone controls, a source-count discrepancy, and the test-induced `.nuxtrc` change restored after inspection. Adam's personal account of these events remains to be added.

**What I'd Do Differently Next Time**

Pending Adam's own words. A useful prompt is how the unanswered maintainer claim and difference between completed practice, local work, and portal submission would change the next contribution's workflow.

---

## Resources Used

- [Issue #274](https://github.com/betterlaspinas/betterlaspinas/issues/274): supplied the icon-contract and visual acceptance criteria; the reproduction recorded discrepancies instead of silently assuming the issue counts were current.
- [Contribution instructions at the tested revision](https://github.com/betterlaspinas/betterlaspinas/blob/7fffa3961785b1b04dd27252650c4c811d22ad5a/CONTRIBUTING.md): guided setup, project checks, and the requirement to wait for assignment or a maintainer thumbs-up.
- [Unit 7 public starter](https://github.com/codepath/ai301-unit7-starter/tree/df8305c2109e7e111994394735bf92ef6dc275ae): used for the ship-gate installation and manifest behavior; it does not substitute for unread portal instructions.
- [Initial reproduction](reproduction/README.md) and [browser/baseline follow-up](reproduction/visual/README.md): preserve commands, actual failures, passing controls, screenshots, and environment limits used in this story.
