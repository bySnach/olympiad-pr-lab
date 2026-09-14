"""CSV import and export helpers for study tasks."""

import csv
from datetime import date
from io import StringIO
from typing import Iterable, List

from .planner import StudyTask


HEADER = "id,title,minutes,priority,due_date,completed"


def export_tasks(tasks: Iterable[StudyTask]) -> str:
    """Serialize tasks to a small CSV document."""
    rows = [HEADER]
    for task in tasks:
        rows.append(
            ",".join(
                [
                    task.task_id,
                    task.title,
                    str(task.minutes),
                    task.priority,
                    task.due_date.isoformat(),
                    str(task.completed).lower(),
                ]
            )
        )
    return "\n".join(rows) + "\n"


def import_tasks(contents: str) -> List[StudyTask]:
    """Read tasks from a CSV document produced by :func:`export_tasks`."""
    reader = csv.DictReader(StringIO(contents))
    tasks = []
    for row in reader:
        tasks.append(
            StudyTask(
                task_id=row["id"],
                title=row["title"],
                minutes=int(row["minutes"]),
                priority=row["priority"],
                due_date=date.fromisoformat(row["due_date"]),
                completed=row["completed"].lower() == "true",
            )
        )
    return tasks
