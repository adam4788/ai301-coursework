# Unit 5 issue-scout — 2026-10-17

Reviewable snapshot of the installed `~/.claude/skills/issue-scout/` tool work. Assignment 5 grades the canonical contribution story, not these tool files. The complete private portal snapshots, raw GitHub capture receipts, prompts, and original CLI envelopes remain local under `.hermes/unit-5/homework/`; none are included here.

## What actually ran

1. Verified the complete Unit 1 backup before overlaying the official three-file starter (`codepath/ai301-unit5-starter`, commit `27e32023dae108fc2a0cb12b4914f3ce19d450b1`). The original rubric, evidence guide and fit-profile paragraph are preserved; the staff frame is unchanged.
2. Executed the four exact commands in `search-strategy.md`; commands, capture times and counts are in `query-execution.json`. Union: **400 fetched → 396 unique → 295 metadata survivors → exactly 5 graded**. `top-five.json` is the actual pre-grading selection. No issue/thread evidence or model call informed the free ranking.
3. On the intended **CodePath Student 2.0 Enterprise** work account, checked a tiny real `sonnet` request returned `OK`. The `sonnet` alias resolved to `claude-sonnet-5` in the real CLI receipts. No personal billing fallback was used.
4. The first tool-driven scan hit the local budget guard without final verdicts; it is recorded as failed, not a completed run. Reused the same cached queries/top five, bounded the missing GitHub evidence reads, and completed the grading stage with a compact source-hashed live evidence payload and the unchanged official rubric. The successful retry and the separate three-URL direct run both exited 0. This was not a second broad search.
5. Saved both complete actual responses verbatim in `scan-output.md`: **5 practice-scan verdicts, then 3 direct course-site verdicts**, all with six checks and final JSON. `run-summary.json` records validated structured results, original failures, model identity and CLI-reported list-price estimates; those estimates are not verified billing charges.

## Results and boundaries

- **Practice scan:** accepts [Perma-Design-Kit #8](https://github.com/tbdal/Perma-Design-Kit/issues/8) and [SigMap #973](https://github.com/manojmallick/sigmap/issues/973); rejects [neo-agent-brain #1078](https://github.com/neomjs/neo-agent-brain/issues/1078), [claude-gateway #615](https://github.com/0xMaxMa/claude-gateway/issues/615), and [claude-code #103018](https://github.com/anthropics/claude-code/issues/103018). A practice-scan acceptance is not permission to select outside the course site. Perma-Design-Kit is fair-source, not fully open-source.
- **Course-site direct run:** accepts [Logixia #120](https://github.com/Logixia/logixia/issues/120); rejects [nanocoder #1631](https://github.com/Nano-Collective/nanocoder/issues/1631) for an active comment-only claim, and [nanocoder #1633](https://github.com/Nano-Collective/nanocoder/issues/1633) for an assignee and open [PR #1645](https://github.com/Nano-Collective/nanocoder/pull/1645).
- No final issue choice, reservation, upstream comment/reaction, reproduction, implementation, PR, or portal submission occurred. Source files were inspected, not executed as an issue reproduction. Do not present the PR author's test claims as our test execution.
- The four-sentence Unit 5 entry is in `beat-2-contribution/contribution-story.md`. Future-unit sections remain untouched, including personal reflection. The preserved rubric was not patched, so no Unit 1 regression-eval score is claimed.

## Verify or repeat

```sh
cd tools/issue-scout
python3 -m unittest -v test_rank_candidates
```

`rank_candidates.rank(batches, captured_at, require_five=True)` is network/model-free. Supply `(query_id, records)` batches in Q1–Q4 order and the saved timezone-aware capture time. It returns drop reasons, conflicts, counts, all ranked survivors, and `top_five`; a shortage of five is an error. Actual raw query outputs are retained locally, not fabricated fixtures.

For a new live search, execute the authored commands again; results will change over time. Before any new paid run, verify `claude-work auth status` still selects the intended work subscription and use a tiny real inference gate. Avoid expensive repeated raw-file reads: reuse already executed free-stage outputs and compact complete live evidence, never a fabricated scan or gold-label substitution. `scan-notes.md` distinguishes actual fixes from proposed future ranking changes.

## Sources used

- [Live Unit 5 Assignment](https://courses.codepath.org/courses/ai301/unit/5#!projects), read signed in on 2026-10-17.
- [Official Unit 5 starter](https://github.com/codepath/ai301-unit5-starter).
- [AI301 Issue Selection site](https://open-source-issue-tracker.onrender.com/?language=TypeScript&language=JavaScript&tag=bug&q=): 100 rendered rows on page 1 of 409 matches; all three direct candidates were present. Languages within that filter are OR; categories combine with AND. No site claim was clicked.
- Actual GitHub issue threads, complete candidate timelines/comments, Development closing-PR fields, current PR states, five default-branch commits, five recent issue response samples per repo, release metadata, complete policy inventories, contributor policies and PR templates, all captured in the local evidence packet.
