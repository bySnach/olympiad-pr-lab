"""Statistical helpers for study tasks."""

from typing import Iterable

from .planner import StudyTask


def median_minutes(tasks: Iterable[StudyTask]) -> float:
    """Return the median duration, or ``0.0`` when no tasks are supplied."""
    values = sorted(task.minutes for task in tasks)
    if not values:
        return 0.0
    return float(values[len(values) // 2])
