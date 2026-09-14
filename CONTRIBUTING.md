# Contributing to Olympiad PR Lab

This repository is an educational contribution exercise. Some functional defects are intentionally present so contributors can practice the full GitHub workflow in a safe, small codebase.

## Contribution rules

1. Pick one open issue or task card.
2. Create a branch named like `fix/search-normalization`.
3. Add a regression test that fails before your change and passes after it.
4. Keep the pull request limited to that issue; do not refactor unrelated code.
5. Run `python -m unittest discover -s tests -v` before opening the pull request.
6. In the pull-request description, write `Closes #<issue-number>` and briefly state the test you added.

## What makes a strong submission

- A small, readable commit history.
- A test that demonstrates the bug rather than only testing a new implementation detail.
- Clear names and standard-library-only code.
- A polite response to review comments, if any.

Do not add dependencies, secrets, network calls, or destructive file operations for these exercises.
