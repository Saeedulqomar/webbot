
from .models import Event
from .serializers import EventSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organizer
from .serializers import OrganizerSerializer

class OrganizerListCreateView(APIView):
    def get(self, request):
        organizers = Organizer.objects.all()
        serializer = OrganizerSerializer(organizers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OrganizerRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return Organizer.objects.get(pk=pk)
        except Organizer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        organizer = self.get_object(pk)
        serializer = OrganizerSerializer(organizer)
        return Response(serializer.data)

    def put(self, request, pk):
        organizer = self.get_object(pk)
        serializer = OrganizerSerializer(organizer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        organizer = self.get_object(pk)
        organizer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EventListCreateView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class EventRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
