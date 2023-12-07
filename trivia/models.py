# trivia/models.py

from django.db import models


class TriviaQuestion(models.Model):
    class CategoryChoices(models.TextChoices):
        SCIENCE = "Science", "Science"
        HISTORY = "History", "History"
        GEOGRAPHY = "Geography", "Geography"
        SPORTS = "Sports", "Sports"
        MUSIC = "Music", "Music"
        # Add more categories as needed

    category = models.CharField(
        max_length=100, choices=CategoryChoices.choices, default=CategoryChoices.SCIENCE
    )
    question = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
