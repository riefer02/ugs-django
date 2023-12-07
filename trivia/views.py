# trivia/views.py

from rest_framework import generics
from .models import TriviaQuestion
from .serializers import TriviaQuestionSerializer

class TriviaQuestionListCreate(generics.ListCreateAPIView):
    queryset = TriviaQuestion.objects.all()
    serializer_class = TriviaQuestionSerializer
