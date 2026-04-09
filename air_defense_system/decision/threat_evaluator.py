"""
Tehdit Değerlendirme
Hedeflerin tehdit seviyesini belirler ve önceliklendirir.
"""

from typing import List, Optional


class ThreatEvaluator:
    """Tehdit değerlendirme sınıfı."""

    THREAT_PRIORITY = {
        "critical": 0,
        "high": 1,
        "medium": 2,
        "low": 3,
        "none": 4,
        "unknown": 5,
    }

    def assess_threat(self, target) -> str:
        """
        Hedefin tehdit seviyesini değerlendirir.

        Args:
            target: Değerlendirilecek hedef

        Returns:
            str: Tehdit seviyesi
        """
        if not hasattr(target, "aircraft"):
            return "unknown"

        aircraft = target.aircraft

        # IFF durumuna göre değerlendir
        if aircraft.iff_status == "friendly":
            return "none"

        if aircraft.iff_status == "hostile":
            # Cisim türüne göre tehdit seviyesi
            threat_map = {
                "F-16": "critical",
                "Helikopter": "high",
                "Drone": "medium",
                "Balon": "low",
                "Kuş": "none",
            }
            return threat_map.get(aircraft.class_name, "medium")

        return "unknown"

    def get_highest_threat(self, targets: List) -> Optional[object]:
        """
        En yüksek tehditli hedefi döndürür.

        Args:
            targets: Hedef listesi

        Returns:
            En tehditli hedef veya None
        """
        if not targets:
            return None

        return min(
            targets,
            key=lambda t: self.THREAT_PRIORITY.get(self.assess_threat(t), 99),
        )

    def rank_threats(self, targets: List) -> List:
        """
        Hedefleri tehdit seviyesine göre sıralar.

        Args:
            targets: Hedef listesi

        Returns:
            List: Sıralanmış hedef listesi
        """
        return sorted(
            targets,
            key=lambda t: self.THREAT_PRIORITY.get(self.assess_threat(t), 99),
        )
