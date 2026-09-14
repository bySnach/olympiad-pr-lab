"""Copy helpers for study tasks."""

from dataclasses import replace

from .planner import StudyTask


def with_title(task: StudyTask, title: str) -> StudyTask:
    """Return an independent copy of ``task`` with a new title."""
    return replace(task, title=title)
