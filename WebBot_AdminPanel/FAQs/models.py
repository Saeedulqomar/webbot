from django.db import models




class Question(models.Model):
    question = models.CharField(max_length=255, unique=True)  # Ensures unique questions
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        indexes = [
            models.Index(fields=['question']),  # Index for fast lookups
        ]
        ordering = ['question']  # Default sorting by question
