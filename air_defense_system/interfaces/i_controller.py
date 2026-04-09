"""
Controller Arayüzü (Interface)
"""

from abc import ABC, abstractmethod


class IController(ABC):
    """Kontrolcü arayüzü."""

    @abstractmethod
    def execute(self, target):
        """Kontrol komutunu yürütür."""
        pass

    @abstractmethod
    def reset(self):
        """Kontrolcüyü sıfırlar."""
        pass

    @abstractmethod
    def set_parameters(self, **kwargs):
        """Parametreleri ayarlar."""
        pass
