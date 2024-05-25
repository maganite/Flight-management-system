from django.db import models
import uuid
import json
from django.utils.translation import gettext_lazy as _


class RiskTypes(models.TextChoices):
    WIND_SPEED_HIGH = 'WS', _('Wind Speed High'),
    PRECIPITATION_HIGH = 'PP', _('Precipitation High'),
    TEMPERATURE_HIGH = 'TM', _('Temperature High'),
    VISIBILITY_LOW = 'VL', _('Visibility Low'),
    TURBULENCE_HIGH = 'TB', _('Turbulence High')


class Recommendation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    risk_type = models.CharField(max_length=100, choices=RiskTypes.choices)
    impact = models.JSONField()
    recommendation = models.JSONField()

    def get_impact_for_risk_type(self, risk_type):
        if self.risk_type == risk_type:
            return self.impact
        else:
            return None

    def get_recommendation_for_risk_type(self, risk_type):
        if self.risk_type == risk_type:
            return self.recommendation
        else:
            return None
