"""
Cisim Veri Modeli
Algılanan hava cisimlerine ait verileri tutar.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Aircraft:
    """Algılanan cisim veri modeli."""

    class_id: int = 0
    class_name: str = ""
    confidence: float = 0.0
    bbox: List[float] = field(default_factory=lambda: [0, 0, 0, 0])
    center_x: float = 0.0
    center_y: float = 0.0
    iff_status: str = "unknown"  # "friendly", "hostile", "unknown"
    speed: Optional[float] = None
    altitude: Optional[float] = None
    track_id: Optional[int] = None

    @property
    def width(self) -> float:
        """Bounding box genişliği."""
        return self.bbox[2] - self.bbox[0]

    @property
    def height(self) -> float:
        """Bounding box yüksekliği."""
        return self.bbox[3] - self.bbox[1]

    @property
    def area(self) -> float:
        """Bounding box alanı."""
        return self.width * self.height

    def __repr__(self):
        return (
            f"Aircraft(class={self.class_name}, conf={self.confidence:.2f}, "
            f"iff={self.iff_status}, pos=({self.center_x:.0f}, {self.center_y:.0f}))"
        )
