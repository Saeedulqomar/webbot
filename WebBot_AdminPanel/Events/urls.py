from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='api_event_list_create'),
    path('<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='api_event_detail'),
]
