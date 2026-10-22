# Rubric: is this a good first issue?

This revision develops the solo calibration checks: active repo/maintainer, bounded specified scope, and unclaimed/no competing work. It separates repository health from maintainer engagement and adds an explicit AI-contribution-policy gate.

## Evidence conventions

In eval mode use only the frozen bundle and measure recency against its capture date. In live mode use the current date and inspect the sources below. Do not treat missing evidence as negative evidence: mark genuinely unavailable evidence `unclear`. An explicit empty assignee/PR list or a completed search finding no policy is evidence, not missing data. Labels, stars, and a polished issue description never override a required failure. Apply the live-only Path Review house rule in scope.md when interpreting student claim comments; do not apply it to eval bundles.

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Maintainer engagement | Eval: last 5 default-branch commits with authors, maintainer first-response sample, and dated OWNER/MEMBER/COLLABORATOR comments. Live: latest 5 default-branch commits (inspect merged PR authors when bots merge), candidate thread, and first maintainer responses on 5 recently updated issues. | At least one human-authored or human-reviewed default-branch change within 90 days, OR at least one human maintainer reply within 90 days in the inspected issue threads. Bot-only automated activity without a human contribution or review does not establish engagement. | required |
| Repository still maintained | Eval: archived flag, latest release, default-branch commit dates, and last push. Live: repository metadata, Releases, and default-branch history. | Repository is not archived AND either a release within 365 days or a default-branch change within 180 days is present. A recent arbitrary-branch push alone is insufficient. No releases is acceptable when the commit condition passes; no minimum star count is required. | required |
| scope-feasible | Issue body: the work it asks for; full thread for context. | The issue describes one identifiable piece of work someone could start: a behavior, a gap, or a task you can point at. It fails only when there is no single piece of work in it: a codebase-wide checklist, an "improve X everywhere", or a container issue tracking many sub-tasks. An open design edge, an "etc.", or several files involved never fails this check; that raises the difficulty note instead. | required |
| Unclaimed / no competing work | Eval: assignees, linked PR states, and dated claim/withdrawal/reopening comments. Live: issue assignees, Development links, timeline, and PRs mentioned in the complete thread. | Issue is open, has no current assignee and no open implementation PR, and has no unreleased claim or progress update within 90 days. A later explicit withdrawal or maintainer invitation for new takers clears an older comment-only claim. Comment-only claims older than 90 days without subsequent progress are stale; age never clears a current assignee or an open PR. Closed-unmerged PRs do not themselves occupy an issue. In live Path Review mode ignore other students' claim comments as scope.md directs, while checking all remaining signals. | required |
| AI-assisted contributions permitted | Eval: contribution-policy text in repo facts. Live: root and .github CONTRIBUTING files, linked contributor policies, dedicated AI policy files, and PR templates. | No applicable explicit ban on AI-generated or AI-assisted contributions. Disclosure, personal understanding, testing, and human-review requirements are conditions to comply with, not bans. Policy silence passes after the listed sources have been checked; inaccessible policy evidence is unclear rather than assumed permission. | required |
| Reproduction or validation starting point | Issue body and thread: example input/output, reproduction steps, acceptance criteria, test names, or exact documentation location. | At least one concrete starting point is supplied: a reproduction input/command, expected output, named regression test, or precise documentation section with the requested correction. | preferred |

## Difficulty note (live mode only)

With each accepted candidate, report a one-line difficulty note in the readable summary:

- **straightforward**: the issue names where the change lives and the change is bounded.
- **moderate**: the location is yours to find, or several files are involved.
- **ambitious**: an open design edge or an unfamiliar subsystem; name the edge so it can be raised with the maintainer early.

The note informs the choice; it never changes accept/reject, never appears in the fenced JSON block, and is skipped entirely in eval mode. This replaces the old scope row only; every other required check and the verdict rule remain unchanged.

## Verdict rule

Return `accept` if and only if every required check is `pass`. Any required `fail` or `unclear` returns `reject`. Execute and report every check even after a failure. Preferred checks never change the verdict. Rank accepted candidates using the fit profile in scope.md; use preferred-check evidence as supporting reasons and as a tie-breaker when personal fit is otherwise comparable. A missing preferred signal is `unclear` and cannot reject an issue. Cite the deciding fact or quote for every grade.
