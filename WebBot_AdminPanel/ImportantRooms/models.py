from django.db import models


class BuildingName(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Prevent duplicate building names

    def __str__(self):
        return self.name

class RoomType(models.Model):
    room_type = models.CharField(max_length=100, unique=True)  # Prevent duplicate room types

    def __str__(self):
        return self.room_type

class ImportantRoom(models.Model):
    room_number = models.CharField(max_length=10)  # Changed to CharField to support alphanumeric room numbers
    location = models.CharField(max_length=255)
    responsibility = models.TextField()  # Optional responsibility field
    room_type = models.ForeignKey(RoomType, related_name='important_rooms', on_delete=models.CASCADE)
    floor_number = models.IntegerField()
    building_name = models.ForeignKey(BuildingName, related_name='important_rooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"Room {self.room_number} in {self.building_name}"

    class Meta:
        indexes = [
            models.Index(fields=['room_number', 'floor_number']),  # Indexing for faster lookup
        ]
        ordering = ['building_name', 'floor_number', 'room_number']  # Default sorting order
