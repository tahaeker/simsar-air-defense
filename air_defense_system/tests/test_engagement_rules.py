"""
Angajman Kuralları Testleri
"""

import unittest
from decision.threat_evaluator import ThreatEvaluator
from models.aircraft import Aircraft
from models.target import Target


class TestEngagementRules(unittest.TestCase):
    """Angajman kuralları testleri."""

    def setUp(self):
        self.evaluator = ThreatEvaluator()

    def test_friendly_no_threat(self):
        aircraft = Aircraft(class_name="F-16", iff_status="friendly", confidence=0.9)
        target = Target(aircraft=aircraft)
        threat = self.evaluator.assess_threat(target)
        self.assertEqual(threat, "none")

    def test_hostile_f16_critical(self):
        aircraft = Aircraft(class_name="F-16", iff_status="hostile", confidence=0.9)
        target = Target(aircraft=aircraft)
        threat = self.evaluator.assess_threat(target)
        self.assertEqual(threat, "critical")

    def test_hostile_drone_medium(self):
        aircraft = Aircraft(class_name="Drone", iff_status="hostile", confidence=0.8)
        target = Target(aircraft=aircraft)
        threat = self.evaluator.assess_threat(target)
        self.assertEqual(threat, "medium")

    def test_bird_no_threat(self):
        aircraft = Aircraft(class_name="Kuş", iff_status="hostile", confidence=0.7)
        target = Target(aircraft=aircraft)
        threat = self.evaluator.assess_threat(target)
        self.assertEqual(threat, "none")

    def test_highest_threat_selection(self):
        targets = [
            Target(aircraft=Aircraft(class_name="Drone", iff_status="hostile")),
            Target(aircraft=Aircraft(class_name="F-16", iff_status="hostile")),
            Target(aircraft=Aircraft(class_name="Balon", iff_status="hostile")),
        ]
        highest = self.evaluator.get_highest_threat(targets)
        self.assertEqual(highest.aircraft.class_name, "F-16")


if __name__ == "__main__":
    unittest.main()
