from django.urls import path

from .views import HealthQuestionnaireAPIView

urlpatterns = [
    path('health-questionnaire/', HealthQuestionnaireAPIView.as_view(), name='health_questionnaire'),

]
