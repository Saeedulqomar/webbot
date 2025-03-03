from django.urls import path
from .views import ClubListCreateView, ClubRetrieveUpdateDestroyView

urlpatterns = [

    path('', ClubListCreateView.as_view(), name='api_club_list_create'),
    path('<int:pk>/', ClubRetrieveUpdateDestroyView.as_view(), name='api_club_detail'),
]
