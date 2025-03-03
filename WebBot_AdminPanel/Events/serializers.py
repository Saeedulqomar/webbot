from rest_framework import serializers
from .models import Organizer, Event


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    organizedBy = OrganizerSerializer()

    class Meta:
        model = Event
        fields = '__all__'
