"""
Cisim → Balon Offset Hesaplayıcı
Cismin ekran merkezine göre offset değerlerini hesaplar.
"""

import math


class OffsetCalculator:
    """Cisim-balon offset hesaplayıcı."""

    def calculate_offset(
        self,
        obj_x: float,
        obj_y: float,
        center_x: float,
        center_y: float,
    ) -> tuple:
        """
        Cismin merkeze göre offset değerlerini hesaplar.

        Args:
            obj_x: Cisim merkez X koordinatı
            obj_y: Cisim merkez Y koordinatı
            center_x: Kare merkez X koordinatı
            center_y: Kare merkez Y koordinatı

        Returns:
            tuple: (offset_x, offset_y)
        """
        offset_x = obj_x - center_x
        offset_y = obj_y - center_y
        return offset_x, offset_y

    def calculate_distance(self, offset_x: float, offset_y: float) -> float:
        """
        Offset vektörünün büyüklüğünü (merkeze uzaklık) hesaplar.

        Args:
            offset_x: X offset değeri
            offset_y: Y offset değeri

        Returns:
            float: Merkeze uzaklık (piksel)
        """
        return math.sqrt(offset_x ** 2 + offset_y ** 2)

    def calculate_angle(self, offset_x: float, offset_y: float) -> float:
        """
        Offset açısını hesaplar (derece cinsinden).

        Args:
            offset_x: X offset değeri
            offset_y: Y offset değeri

        Returns:
            float: Açı (derece)
        """
        return math.degrees(math.atan2(offset_y, offset_x))
