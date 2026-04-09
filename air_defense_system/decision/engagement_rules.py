"""
Angajman Kuralları
Hangi hedeflere angajman yapılacağını belirleyen kurallar.
"""

from core.context import Context
from decision.base_decision import BaseDecisionMaker
from decision.threat_evaluator import ThreatEvaluator
from models.engagement import Engagement


class EngagementRules(BaseDecisionMaker):
    """Angajman kural motoru."""

    def __init__(self):
        self.threat_evaluator = ThreatEvaluator()
        self.min_confidence = 0.6
        self.max_friendly_fire_risk = 0.1
        self.engagement_distance_threshold = 50.0  # piksel

    def evaluate(self, context: Context):
        """
        Durumu değerlendirip angajman kararı verir.

        Args:
            context: Pipeline bağlamı

        Returns:
            Engagement veya None
        """
        if not context.targets:
            return None

        # En yüksek tehditli hedefi bul
        priority_target = self.threat_evaluator.get_highest_threat(context.targets)

        if priority_target is None:
            return None

        if not self.should_engage(priority_target):
            return None

        return Engagement(
            target=priority_target,
            approved=True,
            threat_level=self.threat_evaluator.assess_threat(priority_target),
            reason="Angajman kuralları karşılandı",
        )

    def should_engage(self, target) -> bool:
        """
        Hedefe angajman yapılıp yapılmayacağını belirler.

        Args:
            target: Değerlendirilecek hedef

        Returns:
            bool: Angajman kararı
        """
        # Dost cisim kontrolü
        if hasattr(target, "aircraft") and target.aircraft.iff_status == "friendly":
            return False

        # Güven eşiği kontrolü
        if hasattr(target, "aircraft") and target.aircraft.confidence < self.min_confidence:
            return False

        # Tehdit seviyesi kontrolü
        threat = self.threat_evaluator.assess_threat(target)
        if threat == "none":
            return False

        return True
