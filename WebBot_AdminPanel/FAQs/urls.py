from django.urls import path
from .views import FaqListCreateView, FaqRetrieveUpdateDestroyView

urlpatterns = [
    path('', FaqListCreateView.as_view(), name='api_question_list_create'),
    path('<int:pk>/', FaqRetrieveUpdateDestroyView.as_view(), name='api_question_detail'),
]
