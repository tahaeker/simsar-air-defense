"""
Soyut Hedef Hesaplayıcı
Tüm hedef hesaplama implementasyonları bu sınıftan türetilir.
"""

from abc import ABC, abstractmethod
from typing import List


class BaseTargetCalculator(ABC):
    """Soyut hedef hesaplayıcı sınıfı."""

    @abstractmethod
    def calculate(self, detections: List) -> List:
        """
        Algılanan cisimlerden hedef pozisyonlarını hesaplar.

        Args:
            detections: Algılanan cisimler listesi

        Returns:
            List: Hesaplanan hedef listesi
        """
        pass

    @abstractmethod
    def get_priority_target(self, targets: List):
        """
        En öncelikli hedefi döndürür.

        Args:
            targets: Hedef listesi

        Returns:
            En yüksek öncelikli hedef
        """
        pass
