# Browser reproduction and baseline follow-up

Target: [betterlaspinas/betterlaspinas#274](https://github.com/betterlaspinas/betterlaspinas/issues/274), unmodified upstream commit `7fffa3961785b1b04dd27252650c4c811d22ad5a`. This extends the [initial data/schema report](../README.md); it does not replace its original logs or claim a fix.

## Setup that actually ran

- macOS 27.0.1 ARM64, Node v26.7.0, pinned pnpm 10.29.2, frozen upstream lockfile.
- The initial npm-registry installation timed out. The same pinned package manager and lockfile installed successfully using `https://registry.npmmirror.com`; no registry settings or dependency versions were committed.
- Nuxt's first setup changed its tracked `.nuxtrc` test-utils setup marker from 4.1.0 to 4.2.0. That generated-only change was restored to the original file; upstream source is clean.
- The locally excluded `CLAUDE.local.md` was included by ESLint despite its Git exclusion. Only that private notes file was formatted; no shared lint rule or source file was changed.
- Browser runs used the local Chrome automation session, production build on `http://127.0.0.1:3106`, and the real unmodified catalog—not injected results. The server was stopped after capture and the port was checked for no listener.

## Baseline controls and outcomes

| Check | Actual outcome | Conditions |
|---|---|---|
| Config validation | Exit 0 | Existing validator still accepts the missing icons; not evidence the requested contract is enforced. |
| ESLint | Exit 0 | Private local notes formatted to the existing rules. |
| TypeScript | Exit 0 | Existing `pnpm typecheck` script. |
| Vitest | **299 passed, 18 files passed; exit 0** | `TZ=UTC`, `NODE_OPTIONS=--no-experimental-webstorage`. |
| Production build | Exit 0 | Same environment plus `NUXT_SITE_URL=https://betterlaspinas.org`, copied from the public `.env.example` as an environment override. |
| HTTP/runtime smoke | All 200 | Business route, certificates route, home, and an actual local JavaScript chunk. |
| Hydration | Observed interaction | The real mobile menu changed from its open/X-icon state to closed/menu-icon state after clicking. |
| Separate issue harness | Still intentional RED | Previously recorded 1 positive control pass / 3 missing-icon contract failures; no fix was made. |

These passing baseline checks are **not** a repaired-issue result. The first ordinary test run had 21 failures: disabling Node 26 native web storage reduced it to 3 date failures, and running those same assertions in UTC made all 299 pass. The build initially failed because a sitemap URL was absent, then passed with the documented site URL. No assertions, tests, or application code were weakened to produce these results. Nonfatal upstream build warnings were retained in local raw receipts.

## Rendered defect, measured without changing the DOM

Full measurements: [layout-metrics.json](layout-metrics.json).

| Route / viewport | Cards inspected | Actual icon state | Measured title offset |
|---|---:|---|---|
| Business / 1280 px | 8 | Every icon has width 0 and `::before` content `none` | Every title starts 8 px after its heading's left edge: an empty flex item plus the 8 px gap. |
| Business / 390 px | 8 | Same missing icons | Same 8 px leading gap. |
| Business / 320 px | 8 | Same missing icons | Same 8 px leading gap. |
| Certificates / 1280 px | 6 | Every icon has a real glyph; first icon width 18 px | First title offset 26 px, consisting of the actual 18 px glyph plus 8 px gap. |

The screenshots were inspected separately: service icons are visibly absent on Business and present on Certificates. The Business titles are consistently indented relative to their description text; this evidence does not establish that different Business cards are randomly misaligned with one another. At 320 px, an unrelated header-link/logo overlap is visible even though document scroll width does not exceed viewport width. That is a separate finding, not part of this proposed fix.

### Actual captures

- [Business desktop, 1280 px](business-desktop.png)
- [Certificates desktop control, 1280 px](certificates-desktop.png)
- [Business mobile, 390 px](business-mobile.png)
- [Business narrow, 320 px](business-narrow.png)

The captured PNGs are viewport screenshots; cards below the viewport are covered by the DOM measurements, not claimed to be visible in the image.

## Home-page control and remaining limits

[Home control](home-popular-services-control.json) records real icon glyphs in the home Popular Services list. At this source revision, that component has its own static icon array, so it is not proof the canonical service catalog is correct. [Hydration control](hydrated-menu-control.json) records an actual menu toggle after the Vue app mounted.

The catalog still contains 45 services and 39 missing icons, versus the issue's 50/44. The maintainer has not yet answered the whitespace-only validation question or approved assignment. No implementation, fork, PR, or additional upstream comment was made. Adam's personal reflection and review of the AI-assisted voice examples remain unanswered; they were not filled in on his behalf.

## Reproduction commands

From an unmodified checkout at the pinned revision, install the declared package manager and frozen dependencies. Normal npm registry access may be used where available; the mirror below is the fallback actually used in this run:

```sh
npm_config_audit=false npm_config_fund=false npx --registry=https://registry.npmmirror.com --yes pnpm@10.29.2 install --frozen-lockfile --registry=https://registry.npmmirror.com
TZ=UTC NODE_OPTIONS=--no-experimental-webstorage npx --offline --registry=https://registry.npmmirror.com --yes pnpm@10.29.2 run test --run
NUXT_SITE_URL=https://betterlaspinas.org TZ=UTC NODE_OPTIONS=--no-experimental-webstorage npx --offline --registry=https://registry.npmmirror.com --yes pnpm@10.29.2 run build
HOST=127.0.0.1 PORT=3106 node .output/server/index.mjs
```

Open `/services/business` and `/services/certificates` at the local origin. Preserve the pinned source, wait for fonts, and compare actual glyphs plus computed icon width, flex gap, and text-range geometry. Stop the server after collecting evidence. Package scripts in the actual run were invoked through the resolved cached pnpm 10.29.2 entry point; no persistent global pnpm installation was needed.
