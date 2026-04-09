"""
Hedef Veri Modeli
Hesaplanan hedef bilgilerini tutar.
"""

from dataclasses import dataclass
from models.aircraft import Aircraft


@dataclass
class Target:
    """Hedef veri modeli."""

    aircraft: Aircraft = None
    offset_x: float = 0.0
    offset_y: float = 0.0
    distance_to_center: float = 0.0
    priority: int = 0
    is_locked: bool = False

    def __repr__(self):
        return (
            f"Target(aircraft={self.aircraft.class_name}, "
            f"offset=({self.offset_x:.1f}, {self.offset_y:.1f}), "
            f"dist={self.distance_to_center:.1f}, locked={self.is_locked})"
        )
