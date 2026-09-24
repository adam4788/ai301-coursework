# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

Record of your claim and reproduction on the issue you chose in Unit 1, and of the
evaluation runs that produced `eval-run.txt`. This file is graded at the path above; a copy
kept anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your identity upstream

**GitHub username**

adam4788

---

## Posted upstream

**Claim comment**

https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56#issuecomment-5805398915

> I'd like to take #56. I'll run the headingless-document example against the current code, record my environment and the actual chunk output here, and then investigate a focused fix that preserves the document text and metadata. I haven't reproduced it locally yet; I'll post my own results before proposing a change.

**Reproduction comment**

https://github.com/codepath/pathreview-ai301-fa26-s3/issues/56#issuecomment-5805899592

I reproduced #56 on macOS 27.0 (Apple Silicon), Python 3.11.16, `tiktoken` 0.14.0, at commit `2f4e82f52efbcfcc57d65b3fa5348672163ca088`.

From a fresh clone of this repo:

```sh
git checkout 2f4e82f52efbcfcc57d65b3fa5348672163ca088
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python tiktoken pytest
.venv/bin/python - <<'PY'
from ingestion.chunking.structural_chunker import StructuralChunker

chunker = StructuralChunker()
text = "This is a plain document with no headings at all. " * 20
print("input_chars:", len(text))
print("headingless_chunks:", len(chunker.chunk(text, {"source": "issue-56-repro"})))
print("heading_control_chunks:", len(chunker.chunk("# Heading\nThis is content.", {"source": "control"})))
PY
.venv/bin/python -m pytest tests/unit/test_structural_chunker.py::TestStructuralChunker::test_document_with_no_headings -q -rx
```

I got:

```text
input_chars: 1000
headingless_chunks: 0
heading_control_chunks: 1
x                                                                        [100%]
XFAIL tests/unit/test_structural_chunker.py::TestStructuralChunker::test_document_with_no_headings - issue #56: structural chunker drops documents with no headings
1 xfailed in 0.10s
```

I expected at least one chunk containing the plain document, but got none. Adding a heading makes the control return one chunk. The existing test is marked as an expected failure, and it failed as expected here. I’ll use this case when I work on the fix.

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. Smoke run (`--limit 3`): 3/3 (partial; not a bar verdict).
2. First full run: 17/20 (below bar; disclosure category 0/1).
3. Targeted recheck (`--only pkg-05,pkg-09,pkg-20,pkg-04,pkg-06,pkg-13`): 6/6 (partial).
4. Confirming full run: 20/20 (all categories matched; this is the saved `eval-run.txt`).

**Package analysis**

`pkg-20`: the first rubric decided **accept**, but the gold label was **reject**. The report did show the exact Ghostty behavior, yet the repo's policy requires disclosure of *all* AI help in issue comments. Our AI-assisted check is help, and neither draft named the tool or extent. I revised the communication check; the confirming run decided **reject**, matching gold.

**Check rationale**

> | Steps followable | Repro report's starting state, essential input properties, commands/actions, and trigger read against issue reproduction context. | A stranger with the stated environment can reconstruct an equivalent input and rerun the same attempt to the observation. Exact fixture bytes are needed only when they affect the outcome; a described minimal input with enough essential properties to recreate it is sufficient. Do not require a particular count of steps or headings. | required |

I changed the earlier rule, which demanded exact fixture text, after it wrongly rejected `pkg-05`. That report describes the parts of `env.yml` that matter to the failure and gives the actual command and output. A reader can make an equivalent input without the original file.

**Trade-offs**

The looser input rule now accepts `pkg-05`, but could accept a report that describes a fixture too vaguely to recreate. The check still asks for the *essential* input properties. I re-ran `pkg-06` as a no-evidence canary and `pkg-04`/`pkg-13` as other reject canaries; all remained rejects in the targeted run and the final full run.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/repro-check/`.
