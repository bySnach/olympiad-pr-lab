"""In-memory planning functions for olympiad study tasks."""

from dataclasses import dataclass
from datetime import date
from typing import Dict, Iterable, List, Optional


@dataclass
class StudyTask:
    task_id: str
    title: str
    minutes: int
    priority: str
    due_date: date
    completed: bool = False


class StudyPlanner:
    """Stores and summarizes a small collection of study tasks."""

    def __init__(self, tasks: Optional[Iterable[StudyTask]] = None) -> None:
        self._tasks: Dict[str, StudyTask] = {}
        for task in tasks or []:
            self.add_task(task)

    def add_task(self, task: StudyTask) -> None:
        """Add a task to the planner."""
        if task.task_id in self._tasks:
            raise ValueError(f"task ID already exists: {task.task_id}")
        self._tasks[task.task_id] = task

    def get_task(self, task_id: str) -> Optional[StudyTask]:
        return self._tasks.get(task_id)

    def all_tasks(self) -> List[StudyTask]:
        return list(self._tasks.values())

    def complete_task(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        if task is None:
            return False
        task.completed = True
        return True

    def search(self, query: str) -> List[StudyTask]:
        """Find tasks whose title contains the supplied query."""
        normalized_query = query.strip().casefold()
        return [
            task
            for task in self.all_tasks()
            if normalized_query in task.title.casefold()
        ]

    def tasks_due_between(self, start: date, end: date) -> List[StudyTask]:
        """Return tasks whose due date lies in the requested date range."""
        return [task for task in self.all_tasks() if start <= task.due_date <= end]

    def average_minutes(self) -> float:
        """Return the average planned duration, rounded to one decimal place."""
        tasks = self.all_tasks()
        if not tasks:
            return 0.0
        return round(sum(task.minutes for task in tasks) / len(tasks), 1)

    def by_priority(self) -> List[StudyTask]:
        """Return tasks in priority order."""
        priority_weight = {"high": 0, "medium": 1, "low": 2}
        return sorted(
            self.all_tasks(), key=lambda task: priority_weight.get(task.priority, 0)
        )
