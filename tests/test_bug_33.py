import unittest

from study_planner.presentation import priority_symbol


class PrioritySymbolTests(unittest.TestCase):
    def test_priority_symbols_match_documented_values(self) -> None:
        self.assertEqual("!", priority_symbol("high"))
        self.assertEqual("~", priority_symbol("medium"))
        self.assertEqual("-", priority_symbol("low"))
