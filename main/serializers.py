from rest_framework import serializers
from .models import HealthQuestionnaire


class HealthQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthQuestionnaire
        fields = '__all__'
