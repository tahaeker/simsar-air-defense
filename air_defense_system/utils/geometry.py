"""
Geometri Hesaplamaları
Mesafe, açı ve pozisyon hesaplama fonksiyonları.
"""

import math
from typing import Tuple


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """İki nokta arası Öklid mesafesi."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_angle(x1: float, y1: float, x2: float, y2: float) -> float:
    """İki nokta arası açı (derece)."""
    return math.degrees(math.atan2(y2 - y1, x2 - x1))


def point_in_rect(px: float, py: float, rect: Tuple[float, float, float, float]) -> bool:
    """Noktanın dikdörtgen içinde olup olmadığını kontrol eder."""
    x1, y1, x2, y2 = rect
    return x1 <= px <= x2 and y1 <= py <= y2


def rect_overlap(rect1: Tuple, rect2: Tuple) -> float:
    """İki dikdörtgenin kesişim oranını (IoU) hesaplar."""
    x1 = max(rect1[0], rect2[0])
    y1 = max(rect1[1], rect2[1])
    x2 = min(rect1[2], rect2[2])
    y2 = min(rect1[3], rect2[3])

    if x2 <= x1 or y2 <= y1:
        return 0.0

    intersection = (x2 - x1) * (y2 - y1)
    area1 = (rect1[2] - rect1[0]) * (rect1[3] - rect1[1])
    area2 = (rect2[2] - rect2[0]) * (rect2[3] - rect2[1])
    union = area1 + area2 - intersection

    return intersection / union if union > 0 else 0.0


def normalize_coordinates(x: float, y: float, width: int, height: int) -> Tuple[float, float]:
    """Koordinatları -1 ile 1 arasına normalize eder."""
    norm_x = (x - width / 2) / (width / 2)
    norm_y = (y - height / 2) / (height / 2)
    return norm_x, norm_y
