from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CampusService
from .serializers import CampusServiceSerializer


# 🚀 List & Create View for CampusService
class CampusServiceListCreateView(generics.ListCreateAPIView):
    queryset = CampusService.objects.all()
    serializer_class = CampusServiceSerializer
    search_fields = ['name', 'contact']  # Enables search functionality
    ordering_fields = ['name']  # Enables ordering options

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🚀 Retrieve, Update & Delete View for CampusService
class CampusServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CampusService.objects.all()
    serializer_class = CampusServiceSerializer
