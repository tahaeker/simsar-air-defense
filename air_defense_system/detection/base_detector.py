"""
Soyut Detector (Base Detector)
Tüm detector implementasyonları bu sınıftan türetilir.
"""

from abc import ABC, abstractmethod
from typing import List


class BaseDetector(ABC):
    """Soyut algılayıcı sınıfı."""

    @abstractmethod
    def detect(self, frame) -> List:
        """
        Verilen karede cisim algılama yapar.

        Args:
            frame: Görüntü karesi

        Returns:
            List: Algılanan cisimlerin listesi
        """
        pass

    @abstractmethod
    def load_model(self, model_path: str):
        """
        Algılama modelini yükler.

        Args:
            model_path: Model dosya yolu
        """
        pass

    @abstractmethod
    def set_confidence(self, threshold: float):
        """
        Güven eşiğini ayarlar.

        Args:
            threshold: Güven eşik değeri (0.0 - 1.0)
        """
        pass
