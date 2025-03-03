from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ImportantRoom
from .serializers import ImportantRoomSerializer

class ImportantRoomListCreateView(APIView):
    def get(self, request):
        important_rooms = ImportantRoom.objects.all()
        serializer = ImportantRoomSerializer(important_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImportantRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ImportantRoomRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return ImportantRoom.objects.get(pk=pk)
        except ImportantRoom.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        important_room = self.get_object(pk)
        serializer = ImportantRoomSerializer(important_room)
        return Response(serializer.data)

    def put(self, request, pk):
        important_room = self.get_object(pk)
        serializer = ImportantRoomSerializer(important_room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        important_room = self.get_object(pk)
        important_room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
