"""Aggregation helpers for study tasks."""

from typing import Dict, Iterable

from .planner import StudyTask


def minutes_by_priority(tasks: Iterable[StudyTask]) -> Dict[str, int]:
    """Return total planned minutes for each priority."""
    totals: Dict[str, int] = {}
    for task in tasks:
        totals[task.priority] = task.minutes
    return totals
