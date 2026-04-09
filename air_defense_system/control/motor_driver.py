"""
Motor Haberleşme
Seri port üzerinden motor sürücülere komut gönderir.
"""

import struct
from typing import Optional


class MotorDriver:
    """Motor sürücü haberleşme sınıfı."""

    def __init__(self, port: str = None, baudrate: int = 115200):
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None

    def connect(self, port: str = None, baudrate: int = None):
        """
        Seri porta bağlanır.

        Args:
            port: Seri port adı (örn: COM3)
            baudrate: İletişim hızı
        """
        import serial
        self.port = port or self.port
        self.baudrate = baudrate or self.baudrate
        self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)

    def disconnect(self):
        """Seri port bağlantısını kapatır."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def send_command(self, x_speed: float, y_speed: float):
        """
        Motor hız komutlarını gönderir.

        Args:
            x_speed: X ekseni hız değeri
            y_speed: Y ekseni hız değeri
        """
        if self.serial_conn is None or not self.serial_conn.is_open:
            return

        # Hız değerlerini sınırla
        x_speed = max(-255, min(255, int(x_speed)))
        y_speed = max(-255, min(255, int(y_speed)))

        # Basit protokol: STX + X_HI + X_LO + Y_HI + Y_LO + ETX
        data = struct.pack(">BhhB", 0x02, x_speed, y_speed, 0x03)
        self.serial_conn.write(data)

    def send_fire_command(self):
        """Ateş komutu gönderir."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.write(b"\x02\xFF\xFF\xFF\xFF\x03")

    @property
    def is_connected(self) -> bool:
        """Bağlantı durumunu döndürür."""
        return self.serial_conn is not None and self.serial_conn.is_open
