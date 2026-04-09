"""
Soyut Karar Verici
Tüm karar verme implementasyonları bu sınıftan türetilir.
"""

from abc import ABC, abstractmethod
from core.context import Context


class BaseDecisionMaker(ABC):
    """Soyut karar verici sınıfı."""

    @abstractmethod
    def evaluate(self, context: Context):
        """
        Mevcut durumu değerlendirerek angajman kararı verir.

        Args:
            context: Pipeline bağlam bilgisi

        Returns:
            Engagement veya None
        """
        pass

    @abstractmethod
    def should_engage(self, target) -> bool:
        """
        Belirli bir hedefle angajmana girilmeli mi?

        Args:
            target: Değerlendirilecek hedef

        Returns:
            bool: Angajman kararı
        """
        pass
