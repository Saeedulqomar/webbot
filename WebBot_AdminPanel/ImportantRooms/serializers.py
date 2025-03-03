from rest_framework import serializers
from .models import ImportantRoom

class ImportantRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantRoom
        fields = '__all__'
