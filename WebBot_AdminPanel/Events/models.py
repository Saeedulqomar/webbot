from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint



class Organizer(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Enforcing unique organizer names
    description = models.TextField(blank=True)  # Optional description

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=255, unique=True)  # Preventing duplicate event names
    description = models.TextField()
    date = models.DateTimeField()
    organized_by = models.ForeignKey(Organizer, related_name="events", on_delete=models.CASCADE)
    venue = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} on {self.date}"

    def clean(self):
        # Prevent duplicate events at the same venue and time
        if Event.objects.filter(date=self.date, venue=self.venue).exists():
            raise ValidationError("An event is already scheduled at this venue on this date.")

    def __str__(self):
        return f"{self.name} on {self.date}"

    class Meta:
        indexes = [
            models.Index(fields=['date']),  # Optimized index for date-based filtering
        ]
        constraints = [
            UniqueConstraint(fields=['date', 'venue'], name='unique_event_per_venue')
        ]
