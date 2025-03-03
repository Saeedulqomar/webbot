from django.urls import path
from .views import CampusServiceListCreateView, CampusServiceRetrieveUpdateDestroyView

urlpatterns = [
    path('', CampusServiceListCreateView.as_view(), name='api_campus_service_list_create'),
    path('<int:pk>/', CampusServiceRetrieveUpdateDestroyView.as_view(), name='api_campus_service_detail'),
]
