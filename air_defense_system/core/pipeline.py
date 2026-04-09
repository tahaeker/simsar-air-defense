"""
Ana İşlem Hattı (Pipeline)
Algılama → Tanımlama → Hedef Hesaplama → Karar → Kontrol akışını yönetir.
"""

from core.context import Context


class Pipeline:
    """Ana işlem hattı sınıfı."""

    def __init__(self, detector, identifier, target_calculator, decision_maker, controller):
        self.detector = detector
        self.identifier = identifier
        self.target_calculator = target_calculator
        self.decision_maker = decision_maker
        self.controller = controller
        self.context = Context()
        self._running = False

    def start(self):
        """Pipeline'ı başlatır."""
        self._running = True

    def stop(self):
        """Pipeline'ı durdurur."""
        self._running = False

    def process_frame(self, frame):
        """
        Tek bir kare için tam işlem hattını çalıştırır.

        Args:
            frame: Kameradan alınan görüntü karesi

        Returns:
            Context: Güncellenmiş bağlam nesnesi
        """
        if not self._running:
            return self.context

        # 1. Algılama
        detections = self.detector.detect(frame)
        self.context.detections = detections

        # 2. Tanımlama (IFF)
        for detection in detections:
            identification = self.identifier.identify(frame, detection)
            detection.iff_status = identification

        # 3. Hedef hesaplama
        targets = self.target_calculator.calculate(detections)
        self.context.targets = targets

        # 4. Karar verme
        engagement = self.decision_maker.evaluate(self.context)
        self.context.engagement = engagement

        # 5. Kontrol
        if engagement and engagement.approved:
            self.controller.execute(engagement.target)

        return self.context

    @property
    def is_running(self):
        return self._running
