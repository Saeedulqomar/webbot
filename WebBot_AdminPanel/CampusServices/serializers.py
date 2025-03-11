from rest_framework import serializers
from .models import CampusService



class CampusServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampusService
        fields = '__all__'  # Corrected
