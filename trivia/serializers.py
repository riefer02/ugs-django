# trivia/serializers.py

from rest_framework import serializers
from .models import TriviaQuestion

class TriviaQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaQuestion
        fields = ['id', 'category', 'question', 'answer']
