"""
Balon Hedef Hesaplama Testleri
"""

import unittest
from targeting.offset_calculator import OffsetCalculator


class TestBalloonTarget(unittest.TestCase):
    """Balon hedef hesaplama testleri."""

    def setUp(self):
        self.calculator = OffsetCalculator()

    def test_center_offset_zero(self):
        offset_x, offset_y = self.calculator.calculate_offset(640, 360, 640, 360)
        self.assertEqual(offset_x, 0)
        self.assertEqual(offset_y, 0)

    def test_positive_offset(self):
        offset_x, offset_y = self.calculator.calculate_offset(800, 500, 640, 360)
        self.assertEqual(offset_x, 160)
        self.assertEqual(offset_y, 140)

    def test_negative_offset(self):
        offset_x, offset_y = self.calculator.calculate_offset(400, 200, 640, 360)
        self.assertEqual(offset_x, -240)
        self.assertEqual(offset_y, -160)

    def test_distance_calculation(self):
        distance = self.calculator.calculate_distance(3, 4)
        self.assertAlmostEqual(distance, 5.0)

    def test_angle_calculation(self):
        angle = self.calculator.calculate_angle(1, 0)
        self.assertAlmostEqual(angle, 0.0)

        angle_90 = self.calculator.calculate_angle(0, 1)
        self.assertAlmostEqual(angle_90, 90.0)


if __name__ == "__main__":
    unittest.main()
