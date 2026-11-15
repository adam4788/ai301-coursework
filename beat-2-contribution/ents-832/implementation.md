# ENTS #832 replacement contribution

Status: published draft PR https://github.com/jlab-sensing/ENTS-backend/pull/878, open and unmerged; explicitly overlaps with #877. AI-assisted work; personal reflections remain for Adam to supply.

## Selection and coordination

Kuhu recommended choosing another course-approved issue while respecting Better Las Piñas's wait-for-assignment rule. ENTS #832 was verified available in the course tracker and on GitHub, then claimed on both. Its contribution guide asks for discussion and a comment before coding, without an explicit assignment wait. The approach comment is https://github.com/jlab-sensing/ENTS-backend/issues/832#issuecomment-6784401766.

Issue: https://github.com/jlab-sensing/ENTS-backend/issues/832
Current base: d45e6491498f0a42554e1145a248e189a12c6cc6
Published head: 3d78439723733f8a7c6ddbc14defa4ae3f4533ee
Local branch: fix/832-generic-equation-history

## Problem and approach

Historical voltage/current aliases resolve to the legacy power table. Generic POWER_VOLTAGE and POWER_CURRENT sensors store readings separately, so valid sensor charts could coexist with an empty derived equation.

The fix introduces a shared generic sensor fallback mapping, uses it in direct historical fetching and central-cache evaluation, and includes generic requests for equation-only layouts. It also covers restored equations referencing cells outside the current selection, whose sensor metadata is unavailable. Missing sensors return empty API payloads.

Compatibility choice: preserve a legacy series if it has any non-null reading (including zero), otherwise use the corresponding generic series. This choice applies to each operand's entire series; it does not fill individual gaps or combine timestamps from conflicting sources. The p/power alias remains a legacy series, not an implicit voltage-times-current calculation. Live behavior is unchanged.

## Reproduction and tests

Before changes, the existing focused equation/catalog baseline passed 38 tests. The initial new regression file was then run against the original source: five cases failed and three compatibility controls passed. Failures covered cached aliases, direct fetching, and equation-only request collection.

Coverage added: v/i and full-name aliases, case-insensitive aliases, direct generic fallback, cache fallback without network calls, all-null legacy direct data, absent generic operands, preserving zero and legacy precedence, unchanged power tokens, deduplicated requests, unknown metadata, and loading/evaluating an equation referencing an unselected cell.

Independent review identified the unselected-cell metadata gap; the implementation and an integration test address it. Final verification on November 11: all 33 frontend test files and 255 tests passed, frontend lint passed, and the production build passed. The new regression file contains 12 tests.

## Limits and remaining work

No browser reproduction, backend suite, Docker environment build, upstream CI pass, or maintainer review has been completed. Draft PR #878 was opened November 15 UTC with explicit authorization. Frontend npm audit reports existing dependency advisories; dependency upgrades are outside this fix. Production build has a chunk-size warning.

The canonical contribution story now separates current ENTS evidence from prior investigation. Prior Better Las Piñas evidence is retained as earlier investigation, not relabeled as ENTS work. Publication approval was supplied for the draft, not a merge. Adam's personal reflections must come from Adam.

## Fresh verification and publication — November 15 UTC

35 frontend files / 271 tests passed; lint and production build passed (chunk-size warning only). Verified draft #878 is open, unmerged, and has one commit / five files / +182 -13. GitHub checks and maintainer feedback remain pending. No course-specific PR-monitor playbook execution is claimed.
