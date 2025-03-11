from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Ensures unique names
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)  # Allows optional image upload
    description = models.TextField(blank=True)  # Optional description
    link = models.URLField(max_length=500, blank=True)  # Optional external link

    def __str__(self):
        return self.name
