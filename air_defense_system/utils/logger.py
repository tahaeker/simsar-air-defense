"""
Loglama Modülü
Uygulama genelinde kullanılan logger yapılandırması.
"""

import logging
import sys
from datetime import datetime


def setup_logger(name: str = "air_defense", level: str = "INFO") -> logging.Logger:
    """
    Logger oluşturur ve yapılandırır.

    Args:
        name: Logger adı
        level: Log seviyesi

    Returns:
        logging.Logger: Yapılandırılmış logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    if not logger.handlers:
        # Konsol handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_format = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

        # Dosya handler
        file_handler = logging.FileHandler(
            f"logs/air_defense_{datetime.now().strftime('%Y%m%d')}.log",
            encoding="utf-8",
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s - %(filename)s:%(lineno)d: %(message)s"
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    return logger
