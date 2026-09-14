"""Calendar-oriented helpers for study tasks."""

from datetime import date, timedelta
from typing import Iterable, List, Optional

from .planner import StudyTask


def days_until(task: StudyTask, today: date) -> int:
    """Return signed calendar days from ``today`` to a task's due date."""
    return (task.due_date - today).days


def is_overdue(task: StudyTask, today: date) -> bool:
    """Return whether a task's due date is before ``today``."""
    return task.due_date < today


def tasks_due_on(tasks: Iterable[StudyTask], target: date) -> List[StudyTask]:
    """Return tasks whose due date is exactly ``target``."""
    return [task for task in tasks if task.due_date == target]


def tasks_due_in_month(
    tasks: Iterable[StudyTask], year: int, month: int
) -> List[StudyTask]:
    """Return tasks due in the supplied calendar month and year."""
    return [
        task
        for task in tasks
        if task.due_date.year == year and task.due_date.month == month
    ]


def next_due_after(
    tasks: Iterable[StudyTask], day: date
) -> Optional[StudyTask]:
    """Return the earliest task due strictly after ``day``, if present."""
    return min(
        (task for task in tasks if task.due_date >= day),
        key=lambda task: task.due_date,
        default=None,
    )


def weekday_count(start: date, end: date) -> int:
    """Count weekdays from ``start`` through ``end``, inclusively."""
    current = start
    count = 0
    while current <= end:
        if current.weekday() < 5:
            count += 1
        current += timedelta(days=1)
    return count


def is_weekend(day: date) -> bool:
    """Return whether a date is Saturday or Sunday."""
    return day.weekday() >= 5
