"""
Angajman Veri Modeli
Angajman karar bilgilerini tutar.
"""

from dataclasses import dataclass, field
from datetime import datetime
from models.target import Target


@dataclass
class Engagement:
    """Angajman veri modeli."""

    target: Target = None
    approved: bool = False
    threat_level: str = "unknown"
    reason: str = ""
    timestamp: datetime = field(default_factory=datetime.now)

    def __repr__(self):
        return (
            f"Engagement(approved={self.approved}, "
            f"threat={self.threat_level}, reason='{self.reason}')"
        )
