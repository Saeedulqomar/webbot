from django.db import models


class Organizer(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Enforcing unique organizer names
    description = models.TextField(blank=True)  # Optional description

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=255, unique=True)  # Preventing duplicate event names
    description = models.TextField(blank=True)  # Optional description
    date = models.DateTimeField()
    organized_by = models.ForeignKey(Organizer, related_name="events", on_delete=models.CASCADE)
    venue = models.CharField(max_length=255)
    event_type = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return f"{self.name} ({self.event_type}) on {self.date}"

    class Meta:
        indexes = [
            models.Index(fields=['date']),  # Optimized index for date-based filtering
        ]
