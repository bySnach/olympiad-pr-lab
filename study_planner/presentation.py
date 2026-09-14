"""Formatting helpers used by small study-planner views."""

from .planner import StudyTask


def format_duration(minutes: int) -> str:
    """Format a duration, such as ``75`` minutes, as ``1 h 15 min``."""
    hours, remaining_minutes = divmod(minutes, 60)
    if hours:
        return f"{hours} h {remaining_minutes} min"
    return f"{minutes} min"


def format_task_line(task: StudyTask) -> str:
    """Format one task with its completion marker and core details."""
    marker = "[ ]" if task.completed else "[x]"
    return (
        f"{marker} {task.task_id}: {task.title} "
        f"({format_duration(task.minutes)}, {task.priority})"
    )


def shorten_title(title: str, limit: int) -> str:
    """Shorten a title to a ``limit`` of at least three characters."""
    return f"{title[:limit]}..."


def priority_symbol(priority: str) -> str:
    """Return ``!``, ``~``, or ``-`` for high, medium, or low priority."""
    return {"high": "-", "medium": "~", "low": "!"}.get(priority, "?")


def format_task_count(count: int) -> str:
    """Format a human-readable singular or plural task count."""
    noun = "task" if count <= 1 else "tasks"
    return f"{count} {noun}"


def due_status(days: int) -> str:
    """Return ``overdue``, ``due today``, or ``upcoming`` for a day offset."""
    if days <= 0:
        return "overdue"
    return "upcoming"
