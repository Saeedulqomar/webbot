from django.db import models


class BuildingName(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Prevent duplicate building names

    def __str__(self):
        return self.name


class ImportantRoom(models.Model):
    ROOM_TYPES = [
        ('CLASSROOM', 'Classroom'),
        ('LAB', 'Laboratory'),
        ('OFFICE', 'Office'),
    ]

    room_number = models.CharField(max_length=10)  # Changed to CharField to support alphanumeric room numbers
    location = models.CharField(max_length=255)
    responsibility = models.TextField(blank=True)  # Optional responsibility field
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, default='CLASSROOM')  # Reduced max_length
    floor_number = models.PositiveIntegerField()  # Ensures only non-negative values
    building_name = models.ForeignKey(BuildingName, related_name='important_rooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"Room {self.room_number} ({self.get_room_type_display()}) in {self.building_name}"

    class Meta:
        indexes = [
            models.Index(fields=['room_number', 'floor_number']),  # Indexing for faster lookup
        ]
        ordering = ['building_name', 'floor_number', 'room_number']  # Default sorting order
