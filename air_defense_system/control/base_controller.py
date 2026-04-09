"""
Soyut Kontrolcü
Tüm kontrol implementasyonları bu sınıftan türetilir.
"""

from abc import ABC, abstractmethod


class BaseController(ABC):
    """Soyut kontrolcü sınıfı."""

    @abstractmethod
    def execute(self, target):
        """
        Hedefe yönelik kontrol komutunu yürütür.

        Args:
            target: Hedef bilgisi
        """
        pass

    @abstractmethod
    def reset(self):
        """Kontrolcüyü sıfırlar."""
        pass

    @abstractmethod
    def set_parameters(self, **kwargs):
        """
        Kontrol parametrelerini ayarlar.

        Args:
            **kwargs: Parametre adı-değer çiftleri
        """
        pass
