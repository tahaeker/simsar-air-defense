"""
Renk Tanımlama (Color Identifier) Testleri
"""

import unittest
import numpy as np
from identification.iff_rules import IFFRules
from utils.color_utils import hsv_in_range


class TestColorIdentifier(unittest.TestCase):
    """Renk tabanlı IFF testleri."""

    def setUp(self):
        self.rules = IFFRules()
        self.rules.add_friendly_rule("mavi", [100, 50, 50], [130, 255, 255])
        self.rules.add_friendly_rule("yeşil", [35, 50, 50], [85, 255, 255])
        self.rules.add_hostile_rule("kırmızı_alt", [0, 50, 50], [10, 255, 255])
        self.rules.add_hostile_rule("kırmızı_üst", [170, 50, 50], [180, 255, 255])

    def test_friendly_blue(self):
        hsv = (115, 200, 200)
        result = any(
            hsv_in_range(hsv, r["hsv_lower"], r["hsv_upper"])
            for r in self.rules.friendly_rules
        )
        self.assertTrue(result)

    def test_hostile_red(self):
        hsv = (5, 200, 200)
        result = any(
            hsv_in_range(hsv, r["hsv_lower"], r["hsv_upper"])
            for r in self.rules.hostile_rules
        )
        self.assertTrue(result)

    def test_unknown_color(self):
        hsv = (50, 20, 20)
        friendly = any(
            hsv_in_range(hsv, r["hsv_lower"], r["hsv_upper"])
            for r in self.rules.friendly_rules
        )
        hostile = any(
            hsv_in_range(hsv, r["hsv_lower"], r["hsv_upper"])
            for r in self.rules.hostile_rules
        )
        self.assertFalse(friendly)
        self.assertFalse(hostile)


if __name__ == "__main__":
    unittest.main()
