from django.urls import path
from .views import ProfessorListCreateView, ProfessorRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProfessorListCreateView.as_view(), name='api_professor_list_create'),
    path('<int:pk>/', ProfessorRetrieveUpdateDestroyView.as_view(), name='api_professor_detail'),
]
