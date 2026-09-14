"""Smoke coverage for the public exercise-module import surface."""

import unittest

from study_planner import (
    aggregation,
    calendar_tools,
    collection_tools,
    copies,
    presentation,
    progress,
    records,
    statistics,
)


class ExerciseModuleTests(unittest.TestCase):
    def test_exercise_modules_are_importable(self) -> None:
        self.assertTrue(callable(progress.completed_task_count))
        self.assertTrue(callable(calendar_tools.days_until))
        self.assertTrue(callable(presentation.format_duration))
        self.assertTrue(callable(collection_tools.take_first))
        self.assertTrue(callable(aggregation.minutes_by_priority))
        self.assertTrue(callable(copies.with_title))
        self.assertTrue(callable(records.task_to_record))
        self.assertTrue(callable(statistics.median_minutes))
