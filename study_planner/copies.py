"""Copy helpers for study tasks."""

from .planner import StudyTask


def with_title(task: StudyTask, title: str) -> StudyTask:
    """Return an independent copy of ``task`` with a new title."""
    task.title = title
    return task
