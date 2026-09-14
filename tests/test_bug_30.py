import unittest

from study_planner.presentation import format_duration


class DurationFormattingTests(unittest.TestCase):
    def test_duration_over_an_hour_shows_remaining_minutes(self) -> None:
        self.assertEqual("1 h 15 min", format_duration(75))
