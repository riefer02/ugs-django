# trivia/urls.py

from django.urls import path
from .views import TriviaQuestionListCreate

urlpatterns = [
    path('questions/', TriviaQuestionListCreate.as_view(), name='trivia-question-list'),
]
