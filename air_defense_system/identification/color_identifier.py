"""
Renk Tabanlı Dost/Düşman Tanımlama
HSV renk analizi ile IFF gerçekleştirir.
"""

import numpy as np
from identification.base_identifier import BaseIdentifier
from identification.iff_rules import IFFRules
from utils.color_utils import extract_dominant_color, hsv_in_range


class ColorIdentifier(BaseIdentifier):
    """Renk tabanlı dost/düşman tanımlayıcı."""

    def __init__(self, rules: IFFRules = None):
        self.rules = rules or IFFRules()

    def load_rules(self, rules_path: str):
        """Renk kurallarını YAML dosyasından yükler."""
        self.rules.load_from_yaml(rules_path)

    def identify(self, frame, detection) -> str:
        """
        Cismin bounding box alanındaki baskın renge göre IFF belirler.

        Args:
            frame: Görüntü karesi
            detection: Algılanan cisim (bbox bilgisi içeren)

        Returns:
            str: "friendly", "hostile" veya "unknown"
        """
        # Bounding box alanını kırp
        x1, y1, x2, y2 = map(int, detection.bbox)
        roi = frame[y1:y2, x1:x2]

        if roi.size == 0:
            return "unknown"

        # Baskın rengi çıkar
        dominant_hsv = extract_dominant_color(roi)

        # Kurallara göre sınıflandır
        for rule in self.rules.friendly_rules:
            if hsv_in_range(dominant_hsv, rule["hsv_lower"], rule["hsv_upper"]):
                return "friendly"

        for rule in self.rules.hostile_rules:
            if hsv_in_range(dominant_hsv, rule["hsv_lower"], rule["hsv_upper"]):
                return "hostile"

        return "unknown"
