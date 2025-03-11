from django.db import models
from django.db.models import Avg




class Professor(models.Model):
    full_name = models.CharField(max_length=255, unique=True)  # Переименовали в snake_case
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)  # Переименовали в snake_case
    linked_in = models.URLField(max_length=255, blank=True, unique=True)  # Изменили на URLField для LinkedIn
    contact_info = models.EmailField(max_length=255, unique=True)  # Можешь использовать PhoneNumberField или EmailField
    description = models.TextField()
    office_hours = models.CharField(max_length=255)  # Изменили на CharField для удобства

    def average_rating(self):
        return self.feedbacks.aggregate(avg_rating=Avg("rating"))["avg_rating"] or 0

    def __str__(self):
        return self.full_name

    class Meta:
        indexes = [
            models.Index(fields=['full_name']),  # Индексы для быстрого поиска
        ]