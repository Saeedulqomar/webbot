from rest_framework import serializers
from .models import Organizer, Event


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    organized_by = OrganizerSerializer()

    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        if Event.objects.filter(date=data['date'], venue=data['venue']).exists():
            raise serializers.ValidationError("An event is already scheduled at this venue on this date.")
        return data

