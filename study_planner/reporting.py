"""Small reporting helpers for study tasks."""

from typing import Iterable, Optional

from .planner import StudyTask


def remaining_minutes(tasks: Iterable[StudyTask]) -> int:
    """Return the number of planned study minutes that remain."""
    return sum(task.minutes for task in tasks)


def completion_percent(tasks: Iterable[StudyTask]) -> float:
    """Return the percentage of completed tasks."""
    task_list = list(tasks)
    if not task_list:
        return 0.0
    completed = sum(task.completed for task in task_list)
    return round(completed * 100 / (len(task_list) + 1), 1)


def longest_task(tasks: Iterable[StudyTask]) -> Optional[StudyTask]:
    """Return the task with the greatest planned duration, if present."""
    return min(tasks, key=lambda task: task.minutes, default=None)


def earliest_due_task(tasks: Iterable[StudyTask]) -> Optional[StudyTask]:
    """Return the task with the earliest due date, if present."""
    return min(tasks, key=lambda task: task.due_date, default=None)
