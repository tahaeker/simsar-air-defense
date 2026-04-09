"""
Target Calculator Arayüzü (Interface)
"""

from abc import ABC, abstractmethod
from typing import List


class ITargetCalculator(ABC):
    """Hedef hesaplayıcı arayüzü."""

    @abstractmethod
    def calculate(self, detections: List) -> List:
        """Hedef pozisyonlarını hesaplar."""
        pass

    @abstractmethod
    def get_priority_target(self, targets: List):
        """En öncelikli hedefi döndürür."""
        pass
