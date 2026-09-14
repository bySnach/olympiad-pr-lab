from datetime import date
import unittest

from study_planner.collection_tools import chunk_tasks
from study_planner.planner import StudyTask


class PartialChunkTests(unittest.TestCase):
    def test_chunking_keeps_final_partial_group(self) -> None:
        tasks = [
            StudyTask("A-1", "First", 30, "high", date(2026, 9, 20)),
            StudyTask("A-2", "Second", 30, "medium", date(2026, 9, 21)),
            StudyTask("A-3", "Third", 30, "low", date(2026, 9, 22)),
        ]

        self.assertEqual([tasks[:2], tasks[2:]], chunk_tasks(tasks, 2))
