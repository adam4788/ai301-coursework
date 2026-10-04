# Unit 3 plan — preserve fully headingless documents (#56)

Status: plan posted and implemented on `fix/56-headingless-documents`; final verification recorded below.

Posted plan: https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56#issuecomment-5976291716

Issue: https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56

My posted reproduction: https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56#issuecomment-5805899592

Baseline: commit `2f4e82f52efbcfcc57d65b3fa5348672163ca088` on my fork, `adam4788/pathreview-ai301-fa26-s3`. Implemented branch: `fix/56-headingless-documents`.

## Diagnosis

My Unit 2 reproduction produced zero chunks for the 1,000-character plain document, while the headed control produced one. The same output was observed again during Unit 3 preparation:

```text
input_chars: 1000
headingless_chunks: 0
heading_control_chunks: 1
```

Code inspection of `StructuralChunker._extract_sections()` shows that regular lines are appended only when `heading_stack` or `current_section_lines` is nonempty. Both begin empty; without a heading neither gets populated. Emission also requires a heading stack. This explains why the document never becomes a section. The unused `current_level` assignment is not itself the cause; deleting it alone would not restore the missing text.

## Scope

In scope: documents with nonempty text and no headings recognized by the existing parser. Represent them as a headingless section and let the existing `chunk()` path handle metadata and the 800-token section threshold. Add focused unit coverage and turn the existing headingless expected-failure case into a passing regression.

Not in scope: text before the first heading in a document that does contain headings; changing Markdown heading recognition; rewriting SemanticChunker, its overlap/token policy, or character-offset semantics; changing ingestion/indexing; unrelated lint cleanup. Prep also reproduced dropped pre-heading text, but this plan explicitly defers that adjacent case. Headed-document behavior stays unchanged.

## Files

- `ingestion/chunking/structural_chunker.py`: the fully headingless section-extraction path.
- `tests/unit/test_structural_chunker.py`: the existing headingless regression plus focused text/metadata and large-input coverage.

No other production files are planned.

## Approach

1. Strengthen the current headingless test to assert retained text, heading metadata, preserved source metadata and unchanged caller metadata. Remove its strict `xfail`, then run it on the unchanged source to observe the expected failure before implementation.
2. In `_extract_sections()`, detect that the document contains no headings recognized by the existing heading regex. For nonempty headingless text, return one section with the same surrounding-whitespace trimming used by existing sections, an empty path, and level 0. Keep the existing extraction logic for any document containing a recognized heading.
3. Reuse `chunk()` unchanged: a small section becomes one chunk; a large section goes through existing semantic sub-chunking. Do not implement a separate fallback chunker or manually duplicate metadata assembly.
4. Add focused coverage incrementally. If a discovered edge case requires changing the declared approach or scope, stop, record the deviation, and rerun plan-check before posting an update or continuing.
5. Review the diff before accepting it; commit and push only the issue-specific branch on my fork. The PR belongs to Unit 4, not this step.

## Test plan

Before and after the fix, rerun the exact 1,000-character headingless input and headed control from my posted reproduction. Expected after: the plain input produces one chunk containing `text.strip()`, and the headed control still produces one. For that plain chunk, `heading_path` is `""`, `heading_level` is `0`, and source metadata remains present; the caller's metadata dictionary is unchanged.

Run the updated headingless regression as a real test, not `xfail`, and verify the same assertions on short multiline plain text. Generate an input above `SECTION_TOKEN_LIMIT` containing uniquely numbered sentences: require multiple nonempty chunks, retention of every numbered sentence, and heading/source metadata on all chunks. Existing semantic overlap and whitespace normalization are allowed; exact reconstruction by concatenating overlapping chunks is not the assertion.

Check empty and whitespace-only input still returns `[]`. Rerun the existing single-heading and nested-heading/hierarchy tests, plus the entire structural and semantic unit test files. Run the broader unit suite if the local dependencies permit; report unavailable dependencies or unrelated failures honestly rather than presenting an unrun suite as passing.

## Risks and unknowns

- Headingless metadata has no existing successful output; using an empty path and level 0 matches the section representation expected by `chunk()` without inventing a heading.
- The existing semantic chunker strips sentence boundaries and may overlap text; this plan preserves content within those existing semantics, not byte-for-byte formatting for large inputs.
- The initial detection adds a heading scan. Use the existing recognition rules so a headed document does not accidentally enter the fallback.
- Adjacent issues such as dropped pre-heading text and semantic token/offset edge cases remain deferred. Report them if encountered; do not silently expand this fix.
- The change is now implemented and locally verified; the test results below are observed outputs, not proposed results.

## Deviations

The posted plan held. Only the two named files changed. The existing heading regex is now compiled once inside `_extract_sections()` and used for both the initial detection and the unchanged headed-document loop. This implements the planned scan without changing the recognition rules; it is not a scope change. The seeded `current_level`/`noqa` lines were left alone.

Adam reviewed and accepted three bounded diffs: the initial test-only regression, the production fallback, and the multiline/large-input tests. The initial regression failed with `assert 0 == 1` before the fix. With the fix, the original reproduction returns one headingless chunk and one headed control chunk; the plain text and source metadata are retained, with empty heading path and level 0.

Verification: 33 structural/semantic tests passed. The full unit suite reported 378 passed, 52 unrelated expected failures, and 5 warnings. Ruff passed; Black's non-writing check reported 110 files unchanged; mypy passed on 76 source files. No expected-failure marker remains for #56. Integration/frontend checks and GitHub PR CI are not claimed: this Unit 3 build changes only Python chunking and tests, and no PR was opened.
