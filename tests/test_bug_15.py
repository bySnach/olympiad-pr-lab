import unittest

from study_planner.validation import has_valid_minutes


class PositiveDurationValidationTests(unittest.TestCase):
    def test_zero_minutes_is_not_a_valid_planned_duration(self) -> None:
        self.assertFalse(has_valid_minutes(0))
        self.assertTrue(has_valid_minutes(1))
