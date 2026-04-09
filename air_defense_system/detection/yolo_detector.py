"""
YOLO Detector İmplementasyonu
Ultralytics YOLO kullanarak cisim algılama.
"""

from typing import List
from detection.base_detector import BaseDetector
from models.aircraft import Aircraft


class YoloDetector(BaseDetector):
    """YOLO tabanlı cisim algılayıcı."""

    def __init__(self, model_path: str = None, confidence: float = 0.5):
        self.model = None
        self.confidence = confidence
        if model_path:
            self.load_model(model_path)

    def load_model(self, model_path: str):
        """YOLO modelini yükler."""
        try:
            from ultralytics import YOLO
            self.model = YOLO(model_path)
        except ImportError:
            raise ImportError("ultralytics kütüphanesi yüklü değil. 'pip install ultralytics' ile yükleyin.")

    def set_confidence(self, threshold: float):
        """Güven eşiğini ayarlar."""
        self.confidence = threshold

    def detect(self, frame) -> List[Aircraft]:
        """
        YOLO ile cisim algılama yapar.

        Args:
            frame: Görüntü karesi

        Returns:
            List[Aircraft]: Algılanan cisimler
        """
        if self.model is None:
            return []

        results = self.model(frame, conf=self.confidence)
        detections = []

        for result in results:
            for box in result.boxes:
                aircraft = Aircraft(
                    class_id=int(box.cls[0]),
                    class_name=result.names[int(box.cls[0])],
                    confidence=float(box.conf[0]),
                    bbox=box.xyxy[0].tolist(),
                    center_x=float((box.xyxy[0][0] + box.xyxy[0][2]) / 2),
                    center_y=float((box.xyxy[0][1] + box.xyxy[0][3]) / 2),
                )
                detections.append(aircraft)

        return detections
