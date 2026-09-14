import unittest

from study_planner.validation import is_known_priority


class PriorityValidationNormalizationTests(unittest.TestCase):
    def test_known_priority_ignores_case_and_surrounding_whitespace(self) -> None:
        self.assertTrue(is_known_priority(" HIGH "))
