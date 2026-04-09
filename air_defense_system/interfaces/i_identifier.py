"""
Identifier Arayüzü (Interface)
"""

from abc import ABC, abstractmethod


class IIdentifier(ABC):
    """Dost/düşman tanımlayıcı arayüzü."""

    @abstractmethod
    def identify(self, frame, detection) -> str:
        """Cismin IFF durumunu belirler."""
        pass

    @abstractmethod
    def load_rules(self, rules_path: str):
        """Kuralları yükler."""
        pass
