from django.urls import path
from .views import ImportantRoomListCreateView, ImportantRoomRetrieveUpdateDestroyView

urlpatterns = [

    path('', ImportantRoomListCreateView.as_view(), name='api_room_list_create'),
    path('<int:pk>/', ImportantRoomRetrieveUpdateDestroyView.as_view(), name='api_room_detail'),
]
