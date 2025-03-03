from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionSerializer

class FaqListCreateView(APIView):
    def get(self, request):
        faqs = Question.objects.all()
        serializer = QuestionSerializer(faqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class FaqRetrieveUpdateDestroyView(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        faq = self.get_object(pk)
        serializer = QuestionSerializer(faq)
        return Response(serializer.data)

    def put(self, request, pk):
        faq = self.get_object(pk)
        serializer = QuestionSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        faq = self.get_object(pk)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
