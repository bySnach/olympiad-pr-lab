# Expected behavior

This document describes the product contract. It intentionally states observable behavior instead of pointing to implementation lines.

## Tasks

- Every task has a unique ID. Adding a second task with an existing ID must be rejected and must not replace the original task.
- A task title may contain spaces, punctuation, and Unicode characters.
- Completing an existing task marks it complete; completing an unknown ID reports that no task was changed.

## Search and date ranges

- Text search ignores letter case and whitespace around the query.
- A date-range search includes both the first and the last calendar day in the requested range.

## Summaries and ordering

- The average duration uses every task exactly once and is rounded to one decimal place.
- Priority order is `high`, then `medium`, then `low`. Tasks of the same priority keep their original relative order.

## CSV files

- Exported files use the CSV format and can be imported by standard CSV readers.
- Exporting and importing must preserve a title containing commas or double quotes.
