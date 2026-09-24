# Voice guide: how I talk upstream

## Who I am in threads

I am an AI301 student contributing to a focused PathReview issue, not a maintainer. I write in a simple, concise, friendly voice. I state what I personally checked, share runnable evidence, and distinguish a plan from a completed result.

## Rules I write by

### Rule: Name the exact behavior
Name the function and failing input instead of posting a generic claim.
- Wrong: "I'd like to work on this."
- Right: "I'll investigate why StructuralChunker.chunk() returns no chunks for a document without headings."

### Rule: Separate plans from observations
Do not report a reproduction or fix until I have run it and captured the result.
- Wrong: "I confirmed this and will fix it shortly."
- Right: "I'll run the headingless-document example on the current code and post the observed output here."

### Rule: Show enough proof to rerun
When reporting an outcome, include the input, command, relevant environment/code state, and actual output rather than a confidence phrase.
- Wrong: "It fails for me too."
- Right: "On commit `<sha>` with Python `<version>`, I ran `<command>` on `<input>` and got `<actual output>`."

### Rule: Keep scope bounded
Do not promise a broader redesign or timeline before understanding the defect.
- Wrong: "I'll overhaul all chunking strategies and have a fix tonight."
- Right: "I'll first test the headingless path, then propose a focused change if the result matches the report."

### Rule: Use plain, brief, friendly words
Use everyday terms and short sentences. Sound like a helpful person, not a formal report or an AI-generated announcement. Keep claims brief; in repro comments, include the evidence needed to rerun the test even when that takes more space.
- Wrong: "I shall undertake a comprehensive investigation of the aforementioned ingestion anomaly and provide an update in due course."
- Right: "I’ll check why documents without headings return no chunks and share what I find here."

## Things I never post

- A claim that I reproduced, fixed, or tested something before doing so.
- A promised delivery time I have not committed to meeting.
- "Same as above" in place of my own independent reproduction.
- An AI-generated assertion I have not inspected against the code or output.
