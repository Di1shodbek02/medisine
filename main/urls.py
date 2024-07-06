from django.urls import path

from .views import HealthQuestionnaireAPIView, UpdateHealthQuestionnaireAPIView

urlpatterns = [
    path('health-questionnaire/', HealthQuestionnaireAPIView.as_view(), name='health_questionnaire'),
    path('update-health-questions/', UpdateHealthQuestionnaireAPIView.as_view(), name='update_health_questions'),
]
