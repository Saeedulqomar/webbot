from rest_framework import serializers
from .models import Feedback
from Professors.models import Professor

class FeedbackSerializer(serializers.ModelSerializer):
    professor_name = serializers.ReadOnlyField(source='professor.full_name')

    class Meta:
        model = Feedback
        fields = ["id", "professor", "professor_name", "name", "comment", "rating", "created_at"]
