"""
PID Kontrolcü İmplementasyonu
Hedefe yönelim için PID kontrol algoritması.
"""

import time
from control.base_controller import BaseController
from control.motor_driver import MotorDriver


class PIDController(BaseController):
    """PID kontrol algoritması."""

    def __init__(self, kp: float = 1.0, ki: float = 0.1, kd: float = 0.05):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self._prev_error_x = 0.0
        self._prev_error_y = 0.0
        self._integral_x = 0.0
        self._integral_y = 0.0
        self._last_time = time.time()

        self.motor_driver = MotorDriver()

    def execute(self, target):
        """
        PID hesaplaması yaparak motor komutları gönderir.

        Args:
            target: Hedef bilgisi (offset_x, offset_y)
        """
        current_time = time.time()
        dt = current_time - self._last_time
        if dt <= 0:
            dt = 0.01

        # X ekseni PID
        error_x = target.offset_x
        self._integral_x += error_x * dt
        derivative_x = (error_x - self._prev_error_x) / dt
        output_x = self.kp * error_x + self.ki * self._integral_x + self.kd * derivative_x

        # Y ekseni PID
        error_y = target.offset_y
        self._integral_y += error_y * dt
        derivative_y = (error_y - self._prev_error_y) / dt
        output_y = self.kp * error_y + self.ki * self._integral_y + self.kd * derivative_y

        # Motor komutları gönder
        self.motor_driver.send_command(output_x, output_y)

        # Önceki hata değerlerini güncelle
        self._prev_error_x = error_x
        self._prev_error_y = error_y
        self._last_time = current_time

    def reset(self):
        """PID değerlerini sıfırlar."""
        self._prev_error_x = 0.0
        self._prev_error_y = 0.0
        self._integral_x = 0.0
        self._integral_y = 0.0
        self._last_time = time.time()

    def set_parameters(self, **kwargs):
        """PID parametrelerini ayarlar."""
        if "kp" in kwargs:
            self.kp = kwargs["kp"]
        if "ki" in kwargs:
            self.ki = kwargs["ki"]
        if "kd" in kwargs:
            self.kd = kwargs["kd"]
