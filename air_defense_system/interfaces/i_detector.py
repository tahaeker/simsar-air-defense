"""
Detector Arayüzü (Interface)
"""

from abc import ABC, abstractmethod
from typing import List


class IDetector(ABC):
    """Algılayıcı arayüzü."""

    @abstractmethod
    def detect(self, frame) -> List:
        """Cisim algılama yapar."""
        pass

    @abstractmethod
    def load_model(self, model_path: str):
        """Model yükler."""
        pass

    @abstractmethod
    def set_confidence(self, threshold: float):
        """Güven eşiği ayarlar."""
        pass
