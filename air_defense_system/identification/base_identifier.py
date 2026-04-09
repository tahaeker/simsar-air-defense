"""
Soyut IFF (Identification Friend or Foe)
Tüm tanımlama implementasyonları bu sınıftan türetilir.
"""

from abc import ABC, abstractmethod


class BaseIdentifier(ABC):
    """Soyut dost/düşman tanımlayıcı."""

    @abstractmethod
    def identify(self, frame, detection) -> str:
        """
        Algılanan cismin dost/düşman durumunu belirler.

        Args:
            frame: Görüntü karesi
            detection: Algılanan cisim bilgisi

        Returns:
            str: "friendly", "hostile" veya "unknown"
        """
        pass

    @abstractmethod
    def load_rules(self, rules_path: str):
        """
        IFF kurallarını yükler.

        Args:
            rules_path: Kural dosyası yolu
        """
        pass
