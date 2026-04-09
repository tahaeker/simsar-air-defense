"""
Uçak Sınıflandırıcı
F16, drone, kuş gibi cisim türlerini sınıflandırır.
"""

from typing import Optional
from models.aircraft import Aircraft


class AircraftClassifier:
    """Cisim türü sınıflandırıcı."""

    CLASS_MAP = {
        0: "F-16",
        1: "Drone",
        2: "Kuş",
        3: "Helikopter",
        4: "Balon",
    }

    THREAT_MAP = {
        "F-16": "high",
        "Drone": "medium",
        "Kuş": "none",
        "Helikopter": "high",
        "Balon": "low",
    }

    def classify(self, aircraft: Aircraft) -> str:
        """
        Cismi sınıflandırır.

        Args:
            aircraft: Algılanan cisim

        Returns:
            str: Cisim türü adı
        """
        return self.CLASS_MAP.get(aircraft.class_id, "Bilinmeyen")

    def get_threat_level(self, class_name: str) -> str:
        """
        Cisim türüne göre tehdit seviyesi döndürür.

        Args:
            class_name: Cisim türü adı

        Returns:
            str: Tehdit seviyesi (high, medium, low, none)
        """
        return self.THREAT_MAP.get(class_name, "unknown")
