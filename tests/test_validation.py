import unittest

from study_planner.validation import has_valid_minutes, is_known_priority


class ValidationTests(unittest.TestCase):
    def test_positive_minutes_are_valid(self) -> None:
        self.assertTrue(has_valid_minutes(30))

    def test_exact_known_priority_is_valid(self) -> None:
        self.assertTrue(is_known_priority("high"))
