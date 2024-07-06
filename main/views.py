from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView

from .models import HealthQuestionnaire
from .serializers import HealthQuestionnaireSerializer


class HealthQuestionnaireAPIView(CreateAPIView):
    queryset = HealthQuestionnaire.objects.all()
    serializer_class = HealthQuestionnaireSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class UpdateHealthQuestionnaireAPIView(UpdateAPIView):
    queryset = HealthQuestionnaire.objects.all()
    serializer_class = HealthQuestionnaireSerializer

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)
        return Response(serializer.data)
