from rest_framework import viewsets
from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackListCreateView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        queryset = Feedback.objects.all()
        professor_id = self.request.query_params.get("professor")
        if professor_id:
            queryset = queryset.filter(professor_id=professor_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save()  # Ensure feedback is saved properly

