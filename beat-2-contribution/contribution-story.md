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

2026-10-21 — Installed the staff voice guard, preserved all prior rules in one shared guide, updated the real-repository scopes, and verified clean-draft PASS, unsupported-result STOP, and actual Claude Code hook blocking; the Upstream examples are explicitly AI-assisted drafts pending my personal review. Fresh scouting rejected three occupied Logixia candidates and accepted two replacement site picks, after which I explicitly chose [Better Las Piñas #274](https://github.com/betterlaspinas/betterlaspinas/issues/274), reserved it on the course site, and approved the [posted claim/request for assignment](https://github.com/betterlaspinas/betterlaspinas/issues/274#issuecomment-6330461055). A broad troubleshooting rule initially blocked a legitimate scope question, so the guide was clarified to distinguish troubleshooting from assignment/scope requests while still blocking invented test results; stale candidates, an overstrict local JSON validator, and two unsuccessful Claude posting attempts were preserved rather than presented as successes. One scoped orientation was distilled into a locally excluded `CLAUDE.local.md`, and the unmodified checkout produced [initial data/schema reproduction evidence](reproduction/README.md): one positive control passed and three icon-contract assertions failed, with visual reproduction, full application checks, maintainer approval, and my personal reflection still pending.

**Unit 7: [one line on the tool work]**

[2-4 sentences: the ship-gate and your gate manifest. What it produced
on your real branch, what fought you, what changed because of it.]

**Unit 8: [one line on the tool work]**

[2-4 sentences: the PR-monitor and your playbook. What it read, what it
drafted, what you did with the draft.]

---

## Why I Chose This Issue

**AI-assisted factual draft for my review; my personal learning goal remains to be written in my own words.**

On October 21 I selected Better Las Piñas #274 after reviewing the recommendation and explicitly approving its reservation and exact claim wording. Last week's accepted Logixia #120 was no longer resolvable, and fresh thread/PR checks rejected Logixia #31, #30, and #35 as occupied; I did not claim over those contributors. The patched scout accepted #274 and Kaoto #3527. #274 has a concrete TypeScript/JSON data-and-validation target with a runnable regression starting point, consistent with the documented fit profile; the Kaoto alternative had a less certain Monaco diagnosis. The full replacement read-out is saved in [unit6-replacement-regrading.md](../tools/issue-scout/unit6-replacement-regrading.md).

The scout helped by reading occupancy beyond assignees: Logixia #30 had no comments or assignee but already had a partial open implementation PR. It is not a substitute for fresh source checks: the chosen issue describes 50 services and 44 missing icons, while the tested revision has 45 and 39, and its home page uses a separate static icon list. Its summary called #274 moderate despite flagging an open validation edge; under the supplied difficulty definition that edge warrants an ambitious caution until clarified, without changing the accept verdict. My [claim/request for assignment](https://github.com/betterlaspinas/betterlaspinas/issues/274#issuecomment-6330461055) is posted and verified as `adam4788`; I am waiting for maintainer approval before implementation.

**Personal reflection pending:** what I hope to learn and why this project interests me, in my own words.

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

At tested upstream revision `7fffa3961785b1b04dd27252650c4c811d22ad5a`, 39 of 45 services omit `icon`; the baseline config check still passes, and the real validator accepts both omitted and empty icon values. The browser spacing symptom has not yet been locally measured.

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

macOS 27.0.1 ARM64, Node v26.7.0, project 1.2.0 at upstream `7fffa3961785b1b04dd27252650c4c811d22ad5a`. The project declares `pnpm@10.29.2`, but pnpm was absent locally; no dependency install/full app startup was performed. The dependency-free actual validator was run directly with Node, and the external harness imports that exact upstream implementation. Complete rerun commands and limitations are in [reproduction/README.md](reproduction/README.md).

**Steps to Reproduce**

1. Clone upstream separately and check out `7fffa3961785b1b04dd27252650c4c811d22ad5a`; leave its source unchanged.
2. Run `node scripts/validate-config.mjs` from that checkout: actual exit 0 despite missing catalog icons.
3. Set `ICON_REPRO_REPO` to that checkout and run the coursework [icon-contract.test.mjs](reproduction/icon-contract.test.mjs) using `node --test`: actual exit 1, one positive control passes and three desired-contract assertions fail.
4. Preserve this as partial data/schema reproduction; do not describe it as visual confirmation or a completed fix.

**Reproduction Evidence**

- **Commit showing reproduction:** no implementation fork/commit yet; maintainer approval is pending. Exact [upstream revision tested](https://github.com/betterlaspinas/betterlaspinas/commit/7fffa3961785b1b04dd27252650c4c811d22ad5a); reproduction artifacts are kept in this course repo.
- **Screenshots/logs:** [full actual RED output](reproduction/initial-red-output.txt), [runnable harness](reproduction/icon-contract.test.mjs), and [environment/rerun report](reproduction/README.md). No browser screenshot yet.
- **My findings:** confirmed missing data and non-enforcement of the requested icon contract, not the full visual symptom. Actual catalog counts and home-page data source differ from the issue's description; these remain explicit clarification points rather than invented results.

**Toolkit**

- Tool: the actual upstream Node validator, a separate Node contract harness, and live `repro-check` grading through Claude-work Sonnet.
- What it produced: actual baseline exit 0, intentional RED with 1 positive control pass / 3 contract failures, and [repro-check accept with all six checks](reproduction/repro-check-output.md).
- Difficulties: pnpm was not installed and no app/browser reproduction was attempted; the issue's catalog count and home data-source description differ from this revision.
- What changed: used the dependency-free validator for the initial evidence, explicitly limited the conclusion to the data/schema facet, and recorded browser/full-suite work as pending rather than claiming it passed. The grade does not authorize implementation or mean the issue is fixed.

---

## Solution Approach

**Analysis**

[Your analysis of the root cause: what is causing the issue, traced
to the files and functions involved.]

**Proposed Solution**

[High-level description of your fix approach, and what you are
deliberately NOT changing.]

**Implementation Plan**

1. [Modify file X to do Y]
2. [Add or change Z]
3. [Update tests]

[Record deviations here as they happen: what changed mid-build and
why. A recorded deviation is honest work; silent drift is not.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Testing Strategy

[What observable checks prove the fix: your reproduction steps re-run
against the built change (before and after), and the repo's own test
suite or checks with the outcome shown. "Tests pass" with nothing
observable named is not a strategy.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Implementation Notes

[A running log, added to as you work. Date each entry. What you
built, decisions you made when you made them, wrong turns included.]

**[Date]**

[Entry]

**[Date]**

[Entry]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Pull Request

**PR Link:** [GitHub PR URL when opened]

**PR Description:** [what the PR says; much of the content above
adapts into it]

**Maintainer Feedback:**

- [Date]: [feedback received, or "none yet"; silence is a normal
  state and costs you nothing]
- [Date]: [how you addressed it]

**Status:** [Awaiting review / Iterating / Merged / Closed. The
status is a fact you record, never a grade: the PR is graded as
opened.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Learnings and Reflections

**Technical Skills Gained**

[What you learned technically, named concretely.]

**Challenges Overcome**

[What was hard and how you solved it; point at the real events, the
Toolkit blocks above are full of them.]

**What I'd Do Differently Next Time**

[Reflection on your process.]

---

## Resources Used

[What actually helped, not a reading list. List things this story
already shows you using: the doc you followed to set the environment
up, the thread that explained the bug, the person who answered you.
One real entry beats ten plausible ones.]

- [Link to documentation that helped]
- [Discussion, issue, or post that helped]
