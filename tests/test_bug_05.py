from datetime import date
import unittest

from study_planner.csv_store import export_tasks, import_tasks
from study_planner.planner import StudyTask


class CsvPunctuationTests(unittest.TestCase):
    def test_csv_round_trips_a_title_with_commas_and_quotes(self) -> None:
        original = StudyTask(
            "V-1", 'Read "vectors, matrices" notes', 45, "medium", date(2026, 9, 22)
        )

        self.assertEqual([original], import_tasks(export_tasks([original])))
