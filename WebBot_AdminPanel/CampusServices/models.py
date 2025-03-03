from django.db import models
from django.core.validators import RegexValidator


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Ensures unique service names
    description = models.TextField(blank=True)  # Optional description

    def __str__(self):
        return self.name


class CampusService(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="campus_services", default=1)

    # Phone number validation
    contact = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message="Enter a valid phone number")],
        blank=True
    )

    def __str__(self):
        return self.name
