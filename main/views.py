from rest_framework.generics import CreateAPIView

from .models import HealthQuestionnaire
from .serializers import HealthQuestionnaireSerializer


class HealthQuestionnaireAPIView(CreateAPIView):
    queryset = HealthQuestionnaire.objects.all()
    serializer_class = HealthQuestionnaireSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
