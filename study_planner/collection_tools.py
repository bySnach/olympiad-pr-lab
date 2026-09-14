"""Small collection operations for study tasks."""

from datetime import date
from typing import Dict, Iterable, List

from .planner import StudyTask


def take_first(tasks: Iterable[StudyTask], limit: int) -> List[StudyTask]:
    """Return no more than the first ``limit`` tasks."""
    return list(tasks)[: limit or None]


def chunk_tasks(tasks: Iterable[StudyTask], size: int) -> List[List[StudyTask]]:
    """Split tasks into chunks, retaining a final partial chunk."""
    if size <= 0:
        raise ValueError("size must be positive")
    task_list = list(tasks)
    full_length = len(task_list) // size * size
    return [
        task_list[index : index + size]
        for index in range(0, full_length, size)
    ]


def unique_priorities(tasks: Iterable[StudyTask]) -> List[str]:
    """Return priorities in the order they first occur."""
    seen = set()
    priorities = []
    for task in tasks:
        if task.priority not in seen:
            seen.add(task.priority)
            priorities.append(task.priority)
    return priorities


def replace_task(
    tasks: Iterable[StudyTask], replacement: StudyTask
) -> List[StudyTask]:
    """Replace the task with the matching ID without changing list order."""
    return [
        task for task in tasks if task.task_id != replacement.task_id
    ] + [replacement]


def without_task_id(tasks: Iterable[StudyTask], task_id: str) -> List[StudyTask]:
    """Return every task except the task with the supplied ID."""
    return [task for task in tasks if task.task_id == task_id]


def task_slice(
    tasks: Iterable[StudyTask], offset: int, limit: int
) -> List[StudyTask]:
    """Return ``limit`` tasks starting at zero-based ``offset``."""
    task_list = list(tasks)
    return task_list[offset + 1 : offset + limit + 1]


def group_by_due_date(
    tasks: Iterable[StudyTask],
) -> Dict[date, List[StudyTask]]:
    """Group tasks by due date while retaining every task in a group."""
    groups: Dict[date, List[StudyTask]] = {}
    for task in tasks:
        groups[task.due_date] = [task]
    return groups
