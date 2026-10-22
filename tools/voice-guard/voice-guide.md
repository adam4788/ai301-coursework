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


## PR title and description

Use an issue-specific title naming the changed behavior. Keep every summary bullet and checked box true of the committed diff and recorded output. State AI help and my own review plainly; disclose deferred work and deviations without claiming that disclosure excuses unrelated changes. Do not tick CI before it has run.

## Upstream: how I talk to maintainers

Draft provenance: these new examples were drafted with AI assistance at Adam's request and are pending his personal review. They are hypothetical examples, not claims that any test, investigation, or public post happened. The earlier PathReview identity describes the sandbox; these rules extend the same concise voice to real open-source repositories.

### Claims I post

#### Rule: Offer a specific first step, not a guaranteed fix

Name the behavior I want to investigate and what I will try first. Do not promise that I have reproduced it, that I can fix it, or that it will be finished by a date before I know that. Only claim an issue after checking that nobody else is working on it.

- Wrong: "I'll take this and have it fixed tonight."
- Right: "I'd like to work on the child logger losing its JSON option. I'll first compare the parent and child output with the same input."

### Questions I ask

#### Rule: Say what I tried and ask one answerable question

When asking for technical troubleshooting help, first check the contribution instructions and relevant discussion, name what I ran, describe the actual result, and ask one focused question. A request for assignment is not a troubleshooting question and does not require an invented test result. For a scope-clarification question, quote the relevant requirement or code instead of pretending to have run a test. Any example mentioning a test result must be replaced with real recorded evidence before posting.

- Wrong: "The tests don't work. Can someone help?"
- Right: "I followed CONTRIBUTING.md and ran npm test before changing anything. The browser logger test failed with [exact error]. Is that expected on the current main branch?"

### Pings I send

#### Rule: Add useful progress instead of pressure

Follow the repository's normal response pace. Only follow up with new evidence, a focused blocker, or an honest status update; do not demand an immediate reply or promise work I have not done.

- Wrong: "Any update? I need a reply today."
- Right: "While waiting, I narrowed the failure to child loggers with JSON enabled. The parent output is unchanged. Would a regression test for that case fit the intended scope?"
