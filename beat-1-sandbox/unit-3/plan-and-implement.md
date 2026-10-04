# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

## Posted upstream

**GitHub username**

adam4788

**Plan comment**

https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56#issuecomment-5976291716

My repro above returned no chunks for the 1,000-character headingless document, while the headed control returned one. In `_extract_sections()`, content is only collected after a heading or an existing buffer, so plain text never becomes a section.

I plan to return one section for a nonempty document with no recognized headings, using an empty heading path and level 0. The existing `chunk()` path will keep handling metadata and semantic splitting for large inputs. The change stays in `structural_chunker.py` and its unit tests; I’m leaving headed documents, text before the first heading, and the semantic chunker’s behavior alone.

I’ll turn the current headingless `xfail` into a real regression, then check retained text, source metadata, unchanged caller metadata, and large plain documents. I’ll rerun my original example: the plain input should produce one chunk containing its text, and the headed control should still produce one. I’ll also rerun the empty-input and heading-hierarchy tests. I haven’t built the change yet.

## Your branch

**Branch**

`fix/56-headingless-documents` on my fork, `adam4788/pathreview-ai301-fa26-s3`.

Branch URL: https://github.com/adam4788/pathreview-ai301-fa26-s3/tree/fix/56-headingless-documents

Verified pushed commit: [`8cac1b13463ec3dec7a4cf2016107ef19baa2ca1`](https://github.com/adam4788/pathreview-ai301-fa26-s3/commit/8cac1b13463ec3dec7a4cf2016107ef19baa2ca1). The remote branch SHA matches the local commit. An independent diff review found no logic or security blockers; its empty/whitespace test suggestion was already covered and those two tests were rerun successfully.

This is the Unit 3 branch, not a PR. The original reproduction is my own comment: https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56#issuecomment-5805899592. The baseline is `2f4e82f52efbcfcc57d65b3fa5348672163ca088`.

**Evidence**

The same reproduction command was run before and after the change from the project root, using its Python 3.11 environment:

```sh
.venv/bin/python -c 'from ingestion.chunking.structural_chunker import StructuralChunker; c=StructuralChunker(); t="This is a plain document with no headings at all. "*20; print("input_chars:",len(t)); print("headingless_chunks:",len(c.chunk(t,{"source":"issue-56-repro"}))); print("heading_control_chunks:",len(c.chunk("# Heading\nThis is content.",{"source":"control"})))'
```

Before, on the unchanged baseline:

```text
input_chars: 1000
headingless_chunks: 0
heading_control_chunks: 1
```

After, on the built branch:

```text
input_chars: 1000
headingless_chunks: 1
heading_control_chunks: 1
```

The posted Unit 2 test command was also repeated:

```sh
.venv/bin/python -m pytest tests/unit/test_structural_chunker.py::TestStructuralChunker::test_document_with_no_headings -q -rx
```

Before, as captured in the original posted reproduction:

```text
x                                                                        [100%]
XFAIL tests/unit/test_structural_chunker.py::TestStructuralChunker::test_document_with_no_headings - issue #56: structural chunker drops documents with no headings
1 xfailed in 0.10s
```

The expected-failure marker was removed and the regression strengthened before changing production code. That test-first run failed for the intended reason:

```text
>       assert len(result) == 1
E       assert 0 == 1
E        +  where 0 = len([])
1 failed in 0.14s
```

After, the now-real regression was run with the equivalent quiet command:

```sh
.venv/bin/python -m pytest tests/unit/test_structural_chunker.py::TestStructuralChunker::test_document_with_no_headings -q
```

```text
.                                                                        [100%]
1 passed in 0.23s
```

Additional observed checks on the plain chunk:

```python
plain = chunker.chunk(text, {"source": "issue-56-repro"})[0]
print("plain_text_retained:", plain.text == text.strip())
print("heading_path:", repr(plain.metadata["heading_path"]))
print("heading_level:", plain.metadata["heading_level"])
print("source:", plain.metadata["source"])
```

```text
plain_text_retained: True
heading_path: ''
heading_level: 0
source: issue-56-repro
```

The added multiline test retains interior newlines while trimming surrounding whitespace. The large-input test verifies an input over the 800-token section limit produces multiple nonempty chunks retaining all 200 uniquely numbered sentences and source/heading metadata. Both also check that the caller's metadata dictionary stays unchanged. Existing headed, hierarchy, empty-input, and semantic tests stay passing.

```sh
.venv/bin/python -m pytest tests/unit/test_structural_chunker.py tests/unit/test_semantic_chunker.py -q
.venv/bin/python -m pytest tests/unit -q -m unit
.venv/bin/ruff check .
.venv/bin/black --check .
.venv/bin/mypy api/ core/ ingestion/ rag/ agent/ safety/
```

Observed results:

```text
33 passed in 0.19s
378 passed, 52 xfailed, 5 warnings in 12.74s
All checks passed!
110 files would be left unchanged.
Success: no issues found in 76 source files
```

The remaining expected failures are other seeded issues; #56 no longer has an expected-failure marker. Warnings include Pydantic/passlib deprecations and AsyncMock coroutine warnings. Integration/frontend checks and GitHub PR CI were not run and are not claimed.

The posted plan held: only `ingestion/chunking/structural_chunker.py` and `tests/unit/test_structural_chunker.py` changed. The same heading regex is compiled once and shared by the initial heading scan and existing extraction loop. That is an implementation detail of the planned scan, not a scope expansion. Text before the first heading and semantic overlap/offset behavior remain deferred. See [plan.md](plan.md) for the plan and deviations record.

## Eval iterations

**Run history**

1. Initial three-package smoke attempt on September 30: all three packages errored because Claude was not logged in. The harness reported `agreement: 0/0 scored items`; this was an authentication failure, not a valid agreement score.
2. Three-package retry that day: all three packages errored again. A direct request identified insufficient Console credit; `0/0` was still not a score. Neither failed attempt wrote the submission transcript.
3. After restoring the CodePath Student 2.0 Enterprise subscription, the three-package smoke run reported **3/3**. This partial run did not establish the full bar or category floor.
4. The confirming full run reported **19/20 scored items**, with no runtime errors. The category results were clear-accept **7/7**, scope-creep **4/4**, thread-convention **1/2**, unbuildable **3/3**, and wrong-cause **4/4**. This passes the 18/20 bar and the at-least-one-match-per-category floor. No rubric/evidence/procedure revisions or additional grading runs followed this result.

The final full run used the unmodified official harness and its pinned Sonnet model:

```sh
# From the official starter's eval/ directory
env -u CLAUDE_CONFIG_DIR python3 run_eval.py \
  --rubric /Users/adamnugroho/.claude/skills/plan-check/rubric.md \
  --evidence /Users/adamnugroho/.claude/skills/plan-check/references/evidence-guide.md \
  --skill /Users/adamnugroho/.claude/skills/plan-check/SKILL.md \
  --save-run /Users/adamnugroho/Projects/ai301-coursework/beat-1-sandbox/unit-3/eval-run.txt \
  --out /Users/adamnugroho/Projects/ai301-unit3-starter/eval/full-restored-20261003.json
```

The untouched harness transcript ends:

```text
categories: clear-accept 7/7  scope-creep 4/4  thread-convention 1/2  unbuildable 3/3  wrong-cause 4/4
agreement: 19/20 scored items  (bar: 18/20: PASS)
```

**Package analysis**

`pkg-20` is the single disagreement. The rubric/skill returned **accept**; the instructor gold label is **reject**. The frozen package's repository policy says:

> All AI usage in any form must be disclosed, stating the tool used and the extent of the assistance; the human in the loop must fully understand the work; AI-assisted issues and comments must be reviewed and edited by a human before submission

The candidate comment contains no such tool/extent disclosure. My evaluator nevertheless passed `stated-conventions`, with this exact evidence:

> No statement in plan or comment indicates AI assistance was used in producing this submission, so the repo's conditional AI-disclosure requirement is not shown violated; the 'AI-proposed solution' in the thread refers to a separate, earlier proposal.

The model treated the author's AI involvement as unestablished, rather than treating the missing disclosure in this policy-bearing package as a blocker. The plan's technical cause, boundary, and tests all passed; the disagreement was the contribution-policy interpretation. The gold label shows that this interpretation missed the intended thread-convention case. I kept the passing 19/20 run and disclosed the miss instead of changing the result or claiming perfect agreement.

**Check rationale**

The uploaded rubric's `stated-conventions` check reads exactly:

> The proposal and comment meet stated requirements relevant to this stage, such as required AI-use disclosure, human-written comment requirements, or required coordination before implementation. Do not invent an AI policy, demand unrelated bug-report-template fields in a plan comment, or treat limited review bandwidth as a total ban. Lack of stated requirements is not a failure.

This wording makes actual repo/thread policy part of readiness, rather than grading only the technical plan. It also rejects the alternative of treating every repo as if it had the same AI policy or every template as mandatory for a plan comment. I kept that distinction; the frozen bundle, not my personal voice guide or the evolving live source issue, supplies the applicable rules. No post-evaluation revision is claimed.

**Trade-offs**

`pkg-20` is the concrete false acceptance this convention check permits when the grader demands evidence of AI use before enforcing disclosure. Tightening it to require disclosure whenever a repo mentions AI rules could catch this package, but could reject a genuinely human-authored comment whose author never used AI. A later revision should make the procedure for unresolved authorship/disclosure explicit, then rerun `pkg-20` alongside the already-agreeing `pkg-04` as a thread-convention canary and confirm with another full run. That revision was not made here.

The current result is not based on assuming that other packages stayed unchanged: the confirming run graded all 20 scored packages, and every other package agreed. All 20 returned valid verdicts; the four calibration packages were not scored. The final uploaded rubric, evidence guide, procedure, and shipped SKILL.md still match the files fingerprinted by the final harness transcript.

### Assistance and review record

The materials and code were AI-assisted with Hermes, and Claude Sonnet ran the course eval and live plan-check. Adam approved the plan/comment before posting, then reviewed and accepted the regression-test, production-fix, and additional-test diffs separately. Claude's live plan-check accepted all seven checks before the plan was posted. No claim is made that the AI-assisted drafts were written without assistance.
