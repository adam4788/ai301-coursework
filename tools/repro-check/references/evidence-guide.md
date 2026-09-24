# Evidence guide: where proof lives in a reproduction package

<!--
THIS IS THE PART YOU WRITE (new this week: Unit 1 handed you this file
finished; the scaffolding fades). The skill uses this guide as its map:
for every kind of proof a rubric check names, this file says WHERE to
find it in a package and WHAT GOOD LOOKS LIKE when you do.

Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the issue context, the repo-facts block, the
  claim comment, the repro report and its parts). In live mode (where
  on GitHub or in the draft: the issue thread, the repo's docs, the
  student's draft comment).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("the versions named match what the
  issue targets, or the difference is called out") over adjectives
  ("environment is thorough").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute; the rubric swap showed you what that feels
like. Write the map you wish your grader had.
-->

## Environment

In an eval bundle, compare the repro report's environment/version/code-state record with the issue context and repo-facts block. In live mode, use the issue body and relevant repo setup docs as the target, then read the student's draft for OS/platform, runtime and dependency versions relevant to the failure, and commit/branch or package revision. Good evidence lets another person know which code and environment generated the artifact; state a mismatch rather than silently treating it as equivalent.

## Steps

In an eval bundle, read the repro report's setup, essential input properties, command sequence, and trigger beside the issue's steps. In live mode, compare the draft with the issue's example, repo SETUP.md, and any needed fixture/config. A reader should be able to reconstruct an equivalent input and reach the same observation. Exact bytes need to be pasted only when they affect the result; a compact runnable snippet or a description of sufficient input properties can work. Headings or step counts are not required.

## Behavior shown

In an eval bundle, locate pasted output, logs, screenshots, or test results in the report; compare the input and result to the issue's exact expected and observed behavior. In live mode, use the issue body and actual draft artifact, not a private local test that the draft never quotes. A claimed confirmation needs an artifact showing the issue's specific behavior, not an adjacent failure. An honest non-reproduction or inconclusive attempt can be ready if it shows the relevant test and contrary output, names the condition it could not achieve, and does not claim to disprove the issue. Narrative assertion without observed output is not enough.

## Honesty

In an eval bundle, compare the report's final wording to its command/input, output, and any stated limitations. In live mode, check the same within the draft a stranger would see. A confirmed report shows the target outcome; a cannot-reproduce report accurately names the target attempted and the contrary output; uncertainty remains uncertainty. Neither a claim of confirmation without an artifact nor a claim of absence after testing a different trigger is supported.

## Comms

In an eval bundle, compare the claim to the issue and thread, and both comments to repo-facts rules for issue comments, templates, contribution policy, and AI-use disclosure. In live mode, inspect the current issue thread plus CONTRIBUTING/docs and any explicit policy before judging the draft. A specific claim says what the author is going to investigate without pretending to have finished. The repro comment stands alone as the author's own result. When a policy requires disclosure of any AI assistance for issue comments, using this AI grading skill to review the draft is itself assistance: require the outgoing comment to identify tool and extent. A PR-only disclosure rule applies to PRs, not comments. For Path Review, classmate claims do not block a student's own claim or independent repro; see scope.md.
