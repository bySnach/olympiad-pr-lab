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

## Reports

- Remaining minutes count unfinished tasks only and are `0` for an empty collection.
- Completion percentage is calculated from all tasks, ranges from `0.0` to `100.0`, and is `0.0` for an empty collection.
- A longest-task report selects the task with the greatest duration and returns no task for an empty collection.
- An earliest-due report selects the task with the earliest date and returns no task for an empty collection.

## Filters and validation

- The unfinished-task filter excludes completed tasks.
- A minimum-duration filter includes a task whose duration equals the requested minimum.
- Priority filtering ignores letter case and whitespace around the requested priority.
- Due-date ordering is chronological, from earliest to latest, and preserves input order for equal dates.
- A valid planned duration is a positive number of minutes; zero is not valid.
- A known priority is `high`, `medium`, or `low` after ignoring surrounding whitespace and letter case.

## Extended progress helpers

- Completed-task count includes only completed tasks.
- Completed minutes include only completed tasks; total planned minutes include every task.
- A collection is all-complete only when it is non-empty and every task is complete.
- The first unfinished task is the first incomplete task in input order; no such task returns no task.
- Completion state is `empty` for no tasks, `open` for only incomplete tasks, `in progress` for a mixture, and `complete` for only completed tasks.

## Calendar helpers

- Days until a due date are signed: a past due date has a negative offset.
- A due date equal to the reference date is not overdue; only earlier dates are overdue.
- A day filter includes only tasks due on the exact requested date.
- A month filter matches both its calendar year and month.
- The next task after a date is due strictly later than that date.
- Weekday count includes both requested endpoints and counts Monday through Friday only.
- Saturday and Sunday are weekends.

## Presentation helpers

- A duration below one hour is shown as `N min`; a longer duration shows hours and remaining minutes, so 75 minutes is `1 h 15 min`.
- A completed task uses `[x]` and an incomplete task uses `[ ]` in a task line.
- A shortened title uses a limit of at least three characters, is unchanged when it fits, and otherwise ends in `...` without exceeding that limit.
- Priority symbols are `!` for high, `~` for medium, and `-` for low.
- Only a count of one uses the singular word `task`; zero and every other count use `tasks`.
- A negative day offset is `overdue`, zero is `due today`, and a positive offset is `upcoming`.

## Collection helpers

- Taking the first `0` tasks returns an empty list.
- Chunking retains a final partial chunk.
- Unique priorities preserve their first-occurrence order.
- Replacing a task preserves the original position of its matching ID.
- Removing a task ID retains every other task.
- A task slice starts at its zero-based offset and returns at most its requested limit.
- Grouping by due date retains every task that shares a date.

## Records and statistics

- Minutes grouped by priority are summed for every task of that priority.
- Retitling a task returns a separate task value and leaves the original unchanged.
- A task record keeps `completed` as a boolean; reading a record without that optional field treats it as `False`.
- Median minutes are `0.0` for no tasks, the middle value for an odd count, and the average of the two middle values for an even count.

