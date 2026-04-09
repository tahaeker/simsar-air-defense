"""
Paylaşılan Veri Yapısı (Context)
Pipeline boyunca paylaşılan durum bilgilerini tutar.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class Context:
    """Pipeline boyunca paylaşılan bağlam nesnesi."""

    detections: List = field(default_factory=list)
    targets: List = field(default_factory=list)
    engagement: Optional[object] = None
    frame_count: int = 0
    timestamp: datetime = field(default_factory=datetime.now)
    system_status: str = "idle"

    def reset(self):
        """Bağlamı sıfırlar."""
        self.detections = []
        self.targets = []
        self.engagement = None
        self.frame_count = 0
        self.timestamp = datetime.now()

    def update_timestamp(self):
        """Zaman damgasını günceller."""
        self.timestamp = datetime.now()
        self.frame_count += 1
