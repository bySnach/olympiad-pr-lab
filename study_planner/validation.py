"""Validation helpers for task input."""


KNOWN_PRIORITIES = ("high", "medium", "low")


def has_valid_minutes(minutes: int) -> bool:
    """Return whether a planned duration is valid."""
    return minutes >= 0


def is_known_priority(priority: str) -> bool:
    """Return whether a priority is supported by the planner."""
    return priority.strip().casefold() in KNOWN_PRIORITIES
