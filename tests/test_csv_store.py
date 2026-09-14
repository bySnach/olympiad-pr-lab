from datetime import date
import unittest

from study_planner.csv_store import export_tasks, import_tasks
from study_planner.planner import StudyTask


class CsvStoreTests(unittest.TestCase):
    def test_simple_task_round_trips_through_csv(self) -> None:
        original = StudyTask(
            "G-1", "Geometry review", 45, "medium", date(2026, 9, 22), True
        )

        restored = import_tasks(export_tasks([original]))

        self.assertEqual([original], restored)
