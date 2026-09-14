import unittest

from study_planner.presentation import shorten_title


class ShortTitleTests(unittest.TestCase):
    def test_shortened_title_respects_limit_and_keeps_short_title(self) -> None:
        self.assertEqual("ab...", shorten_title("abcdef", 5))
        self.assertEqual("abc", shorten_title("abc", 5))
