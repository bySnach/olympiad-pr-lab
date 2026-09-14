# Contributing to Olympiad PR Lab

This repository is an educational contribution exercise. Some functional defects are intentionally present so contributors can practice the full GitHub workflow in a safe, small codebase.

## Contribution rules

1. Pick one open issue or task card.
2. Create a branch named like `fix/search-normalization`.
3. For a `BUG` card, add a regression test that fails before your change and passes after it.
4. For a `TEST` card, add only the focused test described by the card; for a `DOC` card, add only the requested documentation.
5. Keep the pull request limited to that issue; do not refactor unrelated code.
6. Run `python -m unittest discover -s tests -v` before opening the pull request.
7. In the pull-request description, write `Closes #<issue-number>` and briefly state the relevant test or documentation evidence.

## Commit shape and olympiad accounting

The full tracker is designed to produce exactly 100 meaningful participant-authored commits when every card is completed in the required shape:

- Every `BUG` card has exactly two commits: a focused `test:` commit that reproduces the documented behavior, followed by a minimal `fix:` commit.
- Every `TEST` card has exactly one focused `test:` commit.
- Every `DOC` card has exactly one focused `docs:` commit.

Do not add cosmetic, empty, or unrelated commits. If review requires a correction, amend the relevant commit or interactively rebase the branch so its required commit count stays intact. The count applies to participant commits in pull-request history; platform-generated merge commits are not part of the olympiad score. Maintainers should use rebase merging so the reviewed commit shape remains visible on `main`.

## What makes a strong submission

- The required small, readable commit history for the selected card.
- A test that demonstrates the bug rather than only testing a new implementation detail.
- Clear names and standard-library-only code.
- A polite response to review comments, if any.

Do not add dependencies, secrets, network calls, or destructive file operations for these exercises.

