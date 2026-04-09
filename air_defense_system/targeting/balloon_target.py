"""
Balon Pozisyon Hesabı
Balonun ekran üzerindeki pozisyonunu ve hedef noktasını hesaplar.
"""

from typing import List, Optional
from targeting.base_target_calc import BaseTargetCalculator
from targeting.offset_calculator import OffsetCalculator
from models.target import Target


class BalloonTarget(BaseTargetCalculator):
    """Balon pozisyon tabanlı hedef hesaplayıcı."""

    def __init__(self, frame_width: int = 1280, frame_height: int = 720):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_center_x = frame_width // 2
        self.frame_center_y = frame_height // 2
        self.offset_calculator = OffsetCalculator()

    def calculate(self, detections: List) -> List[Target]:
        """
        Algılanan cisimlerden hedef pozisyonlarını hesaplar.

        Args:
            detections: Algılanan cisimler

        Returns:
            List[Target]: Hedef listesi
        """
        targets = []

        for detection in detections:
            if detection.iff_status == "friendly":
                continue

            offset_x, offset_y = self.offset_calculator.calculate_offset(
                detection.center_x,
                detection.center_y,
                self.frame_center_x,
                self.frame_center_y,
            )

            target = Target(
                aircraft=detection,
                offset_x=offset_x,
                offset_y=offset_y,
                distance_to_center=self.offset_calculator.calculate_distance(
                    offset_x, offset_y
                ),
            )
            targets.append(target)

        return targets

    def get_priority_target(self, targets: List[Target]) -> Optional[Target]:
        """
        En yakın ve en öncelikli hedefi döndürür.

        Args:
            targets: Hedef listesi

        Returns:
            Target veya None
        """
        if not targets:
            return None

        return min(targets, key=lambda t: t.distance_to_center)
