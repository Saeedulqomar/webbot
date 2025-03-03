from django.urls import path
from .views import CourseListCreateView, CourseRetrieveUpdateDestroyView

urlpatterns = [
    # Для курсов
    path('', CourseListCreateView.as_view(), name='api_course_list_create'),
    path('<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='api_course_detail'),
]
