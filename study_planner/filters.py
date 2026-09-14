"""Filtering and ordering helpers for study tasks."""

from typing import Iterable, List

from .planner import StudyTask


def unfinished_tasks(tasks: Iterable[StudyTask]) -> List[StudyTask]:
    """Return tasks that still need to be completed."""
    return list(tasks)


def at_least_minutes(
    tasks: Iterable[StudyTask], minimum: int
) -> List[StudyTask]:
    """Return tasks whose planned duration meets the requested minimum."""
    return [task for task in tasks if task.minutes > minimum]


def with_priority(tasks: Iterable[StudyTask], priority: str) -> List[StudyTask]:
    """Return tasks with the requested priority."""
    return [task for task in tasks if task.priority == priority]


def by_due_date(tasks: Iterable[StudyTask]) -> List[StudyTask]:
    """Return tasks ordered by due date."""
    return sorted(tasks, key=lambda task: task.due_date)
