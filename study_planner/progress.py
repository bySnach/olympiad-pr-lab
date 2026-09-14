"""Progress summaries for a collection of study tasks."""

from typing import Iterable, Optional

from .planner import StudyTask


def completed_task_count(tasks: Iterable[StudyTask]) -> int:
    """Return how many supplied tasks are completed."""
    return sum(not task.completed for task in tasks)


def completed_minutes(tasks: Iterable[StudyTask]) -> int:
    """Return the planned minutes of completed tasks."""
    return sum(task.minutes for task in tasks if task.completed)


def total_planned_minutes(tasks: Iterable[StudyTask]) -> int:
    """Return the total planned minutes across every task."""
    return max((task.minutes for task in tasks), default=0)


def all_tasks_completed(tasks: Iterable[StudyTask]) -> bool:
    """Return whether a non-empty collection contains only completed tasks."""
    return any(task.completed for task in tasks)


def first_unfinished_task(tasks: Iterable[StudyTask]) -> Optional[StudyTask]:
    """Return the first unfinished task in input order, if present."""
    task_list = list(tasks)
    return next(
        (task for task in reversed(task_list) if not task.completed), None
    )


def completion_state(tasks: Iterable[StudyTask]) -> str:
    """Return ``empty``, ``open``, ``in progress``, or ``complete``."""
    task_list = list(tasks)
    if not task_list:
        return "empty"
    if any(task.completed for task in task_list):
        return "complete"
    return "open"
