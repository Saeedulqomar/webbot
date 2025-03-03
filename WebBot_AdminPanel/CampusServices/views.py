from .models import CampusService
from .serializers import CampusServiceSerializer

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Service
from .serializers import ServiceSerializer

class ServiceListCreateView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ServiceRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class CampusServiceListCreateView(APIView):
    def get(self, request):
        campus_services = CampusService.objects.all()
        serializer = CampusServiceSerializer(campus_services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CampusServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CampusServiceRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return CampusService.objects.get(pk=pk)
        except CampusService.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        campus_service = self.get_object(pk)
        serializer = CampusServiceSerializer(campus_service)
        return Response(serializer.data)

    def put(self, request, pk):
        campus_service = self.get_object(pk)
        serializer = CampusServiceSerializer(campus_service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        campus_service = self.get_object(pk)
        campus_service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
