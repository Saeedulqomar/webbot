from rest_framework import serializers
from .models import Service, CampusService


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class CampusServiceSerializer(serializers.ModelSerializer):
    serviceType = ServiceSerializer()  # Вложенный сериализатор для типа услуги

    class Meta:
        model = CampusService
        fields = '__all__'
