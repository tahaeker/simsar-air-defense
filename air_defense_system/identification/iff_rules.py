"""
IFF Kural Tanımları
Renk aralıklarına göre dost/düşman kurallarını yönetir.
"""

import yaml
from typing import List, Dict


class IFFRules:
    """IFF kural yöneticisi."""

    def __init__(self):
        self.friendly_rules: List[Dict] = []
        self.hostile_rules: List[Dict] = []
        self.default_classification: str = "unknown"

    def load_from_yaml(self, path: str):
        """
        YAML dosyasından kuralları yükler.

        Args:
            path: YAML dosya yolu
        """
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        iff = data.get("iff_rules", {})
        self.friendly_rules = iff.get("friendly", [])
        self.hostile_rules = iff.get("hostile", [])
        self.default_classification = data.get("default_classification", "unknown")

    def add_friendly_rule(self, name: str, hsv_lower: list, hsv_upper: list):
        """Dost kuralı ekler."""
        self.friendly_rules.append({
            "name": name,
            "hsv_lower": hsv_lower,
            "hsv_upper": hsv_upper,
        })

    def add_hostile_rule(self, name: str, hsv_lower: list, hsv_upper: list):
        """Düşman kuralı ekler."""
        self.hostile_rules.append({
            "name": name,
            "hsv_lower": hsv_lower,
            "hsv_upper": hsv_upper,
        })
