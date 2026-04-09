"""
Decision Maker Arayüzü (Interface)
"""

from abc import ABC, abstractmethod
from core.context import Context


class IDecisionMaker(ABC):
    """Karar verici arayüzü."""

    @abstractmethod
    def evaluate(self, context: Context):
        """Durumu değerlendirip karar verir."""
        pass

    @abstractmethod
    def should_engage(self, target) -> bool:
        """Angajman kararı verir."""
        pass
