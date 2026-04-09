"""
Renk Analiz Yardımcıları
HSV renk uzayında analiz fonksiyonları.
"""

import cv2
import numpy as np
from typing import Tuple, List


def extract_dominant_color(roi: np.ndarray) -> Tuple[int, int, int]:
    """
    ROI alanındaki baskın HSV rengini çıkarır.

    Args:
        roi: İlgi alanı görüntüsü (BGR)

    Returns:
        Tuple[int, int, int]: Baskın HSV değeri (H, S, V)
    """
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    h_mean = int(np.mean(hsv[:, :, 0]))
    s_mean = int(np.mean(hsv[:, :, 1]))
    v_mean = int(np.mean(hsv[:, :, 2]))
    return (h_mean, s_mean, v_mean)


def hsv_in_range(
    hsv: Tuple[int, int, int],
    lower: List[int],
    upper: List[int],
) -> bool:
    """
    HSV değerinin belirtilen aralıkta olup olmadığını kontrol eder.

    Args:
        hsv: Kontrol edilecek HSV değeri
        lower: Alt sınır [H, S, V]
        upper: Üst sınır [H, S, V]

    Returns:
        bool: Aralıkta ise True
    """
    return (
        lower[0] <= hsv[0] <= upper[0]
        and lower[1] <= hsv[1] <= upper[1]
        and lower[2] <= hsv[2] <= upper[2]
    )


def get_color_name(hsv: Tuple[int, int, int]) -> str:
    """
    HSV değerine göre renk adı döndürür.

    Args:
        hsv: HSV değeri

    Returns:
        str: Renk adı
    """
    h, s, v = hsv

    if s < 50:
        if v < 50:
            return "siyah"
        elif v > 200:
            return "beyaz"
        else:
            return "gri"

    if h < 10 or h > 170:
        return "kırmızı"
    elif 10 <= h < 25:
        return "turuncu"
    elif 25 <= h < 35:
        return "sarı"
    elif 35 <= h < 85:
        return "yeşil"
    elif 85 <= h < 130:
        return "mavi"
    elif 130 <= h < 170:
        return "mor"

    return "bilinmeyen"
