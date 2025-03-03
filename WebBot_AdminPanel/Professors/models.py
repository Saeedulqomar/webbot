from django.db import models


class Professor(models.Model):
    full_name = models.CharField(max_length=255)  # Переименовали в snake_case
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)  # Переименовали в snake_case
    linked_in = models.URLField(max_length=255, blank=True)  # Изменили на URLField для LinkedIn
    contact_info = models.EmailField(max_length=255, blank=True)  # Можешь использовать PhoneNumberField или EmailField
    course = models.ForeignKey('Courses.Course', related_name='professors', on_delete=models.CASCADE)  # Переименовали в snake_case
    description = models.TextField()
    office_hours = models.CharField(max_length=255)  # Переименовали в snake_case

    def __str__(self):
        return self.full_name

    class Meta:
        indexes = [
            models.Index(fields=['full_name', 'course']),  # Индексы для быстрого поиска
        ]