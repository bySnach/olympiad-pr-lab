# Exercise module map

The study-planner exercise keeps each small responsibility in a dedicated
standard-library-only module:

- `planner.py` defines tasks and the in-memory planner, including search,
  range, average, and priority helpers.
- `reporting.py` provides remaining-work, completion, longest-task, and
  earliest-due reports.
- `filters.py` contains task filters and due-date ordering.
- `validation.py` validates planned minutes and priorities.
- `csv_store.py` imports and exports task collections as CSV.
- `progress.py` summarizes task completion and planned minutes.
- `calendar_tools.py` contains date, overdue, weekday, and weekend helpers.
- `presentation.py` formats durations, task lines, labels, and symbols.
- `collection_tools.py` handles task list slicing, grouping, replacement, and
  chunking.
- `aggregation.py` totals minutes by priority.
- `copies.py` returns independent task copies with updated titles.
- `records.py` converts tasks to and from simple records.
- `statistics.py` calculates median planned minutes.
