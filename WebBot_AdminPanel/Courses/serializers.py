from rest_framework import serializers
from .models import Course
from Professors.serializers import ProfessorSerializer  # Сериализатор для профессора


class CourseSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer()  # Вложенный сериализатор для профессора

    class Meta:
        model = Course
        fields = '__all__'
