from django.db import models

from accounts.models import User


class HealthQuestionnaire(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chest_pain = models.BooleanField()
    spreading_pains = models.BooleanField()
    headaches = models.BooleanField()
    difficulty_breathing = models.BooleanField()
    lost_consciousness = models.BooleanField()
    alcohol_consumption = models.BooleanField()
    smoking = models.BooleanField()
    water_consumption = models.BooleanField()
    physically_active = models.BooleanField()
    blood_pressure = models.CharField(max_length=20)  # You may need to adjust max_length
