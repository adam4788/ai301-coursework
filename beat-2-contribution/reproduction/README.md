# Initial reproduction: missing service icons and missing validation

**Historical initial report.** Browser reproduction and controlled baseline checks were subsequently completed: see [the follow-up with real screenshots and measurements](visual/README.md). The limits below describe the first attempt, not the latest state.

Issue: https://github.com/betterlaspinas/betterlaspinas/issues/274

Claim/request for assignment: https://github.com/betterlaspinas/betterlaspinas/issues/274#issuecomment-6330461055

Follow-up posted and verified as `adam4788`: https://github.com/betterlaspinas/betterlaspinas/issues/274#issuecomment-6484502126

The AI-assisted follow-up passed the voice guard and shared the independently rerun catalog count:

````text
Hi! Following up on my request to work on this. With AI assistance, on macOS ARM64 and Node v26.7.0, I checked the unmodified checkout at `7fffa3961785b1b04dd27252650c4c811d22ad5a`. From the repo root I ran:

```sh
node -e 'const {services}=require("./app/config/services.json"); console.log(`services=${services.length} missing_icons=${services.filter(s => !s.icon).length}`)'
```

It printed `services=45 missing_icons=39`, rather than the 50 and 44 mentioned in the issue.

Is this issue still available for me to work on? Thanks!
````

Captured: 2026-10-21, America/Phoenix. The initial report below is local coursework evidence, not a fix; the later follow-up is quoted above.

## Environment and code state

- macOS 27.0.1, ARM64; Node v26.7.0.
- Unmodified upstream checkout: `7fffa3961785b1b04dd27252650c4c811d22ad5a` on `main`.
- Project version: 1.2.0; declared Node >=22 and package manager `pnpm@10.29.2`.
- `pnpm` was not installed locally. No package install, Nuxt startup, application build, or full lint/typecheck/Vitest suite was performed. The real configuration validator is dependency-free, so it was run directly through Node.
- No production data, schema, renderer, or upstream tests were edited. The separate test file in this coursework repository is a clearly labeled reproduction harness.

## Target and important distinctions

The issue asks for non-empty icons in the canonical catalog, a required schema/type property, aligned category cards, home-page spot checks, and all standard checks passing.

At this exact revision there are **45 services: 6 with icons and 39 missing**, not the issue's 50/44. Preserve the discrepancy rather than changing the reported count to match the issue. Also, `app/components/home/PopularServices.vue` currently has a separate static, typed icon list; the source does not establish the issue's suggestion that it reads this same catalog.

## Rerun the same attempt

From this coursework checkout, set the path of a separate unmodified target checkout:

```sh
COURSE_REPO="$PWD"
git clone https://github.com/betterlaspinas/betterlaspinas.git ../betterlaspinas-274
UPSTREAM_REPO="$(cd ../betterlaspinas-274 && pwd)"
git -C "$UPSTREAM_REPO" checkout 7fffa3961785b1b04dd27252650c4c811d22ad5a
(cd "$UPSTREAM_REPO" && node scripts/validate-config.mjs)
ICON_REPRO_REPO="$UPSTREAM_REPO" node --test "$COURSE_REPO/beat-2-contribution/reproduction/icon-contract.test.mjs"
```

Use a different empty clone directory if `../betterlaspinas-274` already exists. No dependency install is needed for these two Node commands. The harness imports upstream's actual `validateAgainstSchema`, reads its actual schema/catalog, and constructs minimal test-only inputs: one valid icon, an omitted icon property, and an empty string. It does not patch upstream.

## Actual observations

The existing validator exited **0**:

```text
✔ Config validation passed (services.json, categories.json, offices.json, agencies.json, officials.json)
```

The external contract tests exited **1**, intentionally RED:

```text
✔ positive control: a service with an icon is accepted by the real validator
✖ every current service has a nonblank icon
✖ the real validator rejects a service with no icon property
✖ the real validator rejects an empty icon value
ℹ tests 4
ℹ pass 1
ℹ fail 3
```

The last two assertions received `true` from the validator where the desired contract expects `false`. The catalog assertion lists the 39 missing service IDs. Actual output (whitespace-only diagnostic lines normalized for Git; raw receipt retained locally): [initial-red-output.txt](initial-red-output.txt). Runnable harness: [icon-contract.test.mjs](icon-contract.test.mjs).

## Conclusion and limits

**Confirmed:** the catalog is missing icons and the current schema/validator accepts omitted and empty icon values. A known-good fixture passes, so the RED result is not a broken test setup. The existing optional `ServiceItem.icon` and schema explain the accepted input; their existence alone does not prove maintainer intent.

**Not confirmed locally:** the rendered phantom gap, category-page baseline alignment, or a home-page visual defect. No screenshot, DOM measurement, full-suite pass, or fixed build is claimed. This is an initial partial reproduction of the data/validation facet, not proof that every symptom in the issue is reproduced.

**Next gates:** wait for maintainer assignment/approval; clarify whitespace-only icon policy and the catalog/home-source discrepancies. Then stand up the app and complete visual reproduction before implementing the agreed change. At the time of this initial report, no additional upstream comment or PR had been posted.

## Assistance

Hermes gathered source evidence and ran the commands; Claude-work Sonnet graded candidates and summarized the scoped subsystem. The reproduction harness and this evidence summary were AI-assisted. Adam chose the issue and approved the exact public claim. Personal learning/reflection remains for Adam to review and write in his own voice.
