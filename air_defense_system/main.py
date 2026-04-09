"""
SIMSAR Hava Savunma Sistemi - Ana Giriş Noktası
"""

import sys
import yaml
from utils.logger import setup_logger
from detection.yolo_detector import YoloDetector
from identification.color_identifier import ColorIdentifier
from identification.iff_rules import IFFRules
from targeting.balloon_target import BalloonTarget
from decision.engagement_rules import EngagementRules
from control.pid_controller import PIDController
from core.pipeline import Pipeline


def load_config(path: str = "config/settings.yaml") -> dict:
    """Yapılandırma dosyasını yükler."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    """Ana fonksiyon."""
    logger = setup_logger("air_defense")
    logger.info("SIMSAR Hava Savunma Sistemi başlatılıyor...")

    # Yapılandırma yükle
    try:
        config = load_config()
    except FileNotFoundError:
        logger.error("Yapılandırma dosyası bulunamadı!")
        sys.exit(1)

    # Bileşenleri oluştur
    detector = YoloDetector(
        model_path=config.get("detection", {}).get("model_path"),
        confidence=config.get("detection", {}).get("confidence_threshold", 0.5),
    )

    iff_rules = IFFRules()
    iff_rules.load_from_yaml("config/color_rules.yaml")
    identifier = ColorIdentifier(rules=iff_rules)

    target_calculator = BalloonTarget(
        frame_width=config.get("camera", {}).get("width", 1280),
        frame_height=config.get("camera", {}).get("height", 720),
    )

    decision_maker = EngagementRules()

    pid_config = config.get("pid", {})
    controller = PIDController(
        kp=pid_config.get("kp", 1.0),
        ki=pid_config.get("ki", 0.1),
        kd=pid_config.get("kd", 0.05),
    )

    # Pipeline oluştur ve başlat
    pipeline = Pipeline(
        detector=detector,
        identifier=identifier,
        target_calculator=target_calculator,
        decision_maker=decision_maker,
        controller=controller,
    )

    pipeline.start()
    logger.info("Sistem hazır. Pipeline çalışıyor.")

    # Kamera döngüsü
    try:
        import cv2
        cap = cv2.VideoCapture(config.get("camera", {}).get("source", 0))

        while pipeline.is_running:
            ret, frame = cap.read()
            if not ret:
                logger.warning("Kare okunamadı!")
                continue

            context = pipeline.process_frame(frame)

            if context.engagement and context.engagement.approved:
                logger.info(
                    f"ANGAJMAN: {context.engagement.target.aircraft.class_name} "
                    f"- Tehdit: {context.engagement.threat_level}"
                )

    except KeyboardInterrupt:
        logger.info("Sistem kapatılıyor...")
    finally:
        pipeline.stop()
        if 'cap' in locals():
            cap.release()
        logger.info("Sistem kapatıldı.")


if __name__ == "__main__":
    main()
