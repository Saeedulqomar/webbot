from rest_framework import serializers
from .models import Professor
from Feedbacks.models import Feedback  # Import feedback for nested serializer
from Feedbacks.serializers import FeedbackSerializer


class ProfessorSerializer(serializers.ModelSerializer):
    feedbacks = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.average_rating()

    class Meta:
        model = Professor
        fields = ["id", "full_name", "photo", "linked_in", "contact_info", "description", "office_hours", "feedbacks", "average_rating"]

    def get_feedbacks(self, obj):
        feedbacks = obj.feedbacks.all()  # Get all related feedback
        return FeedbackSerializer(feedbacks, many=True).data  # Serialize feedbacks
