from django.urls import path
from .views import ProfessorListView, ProfessorDetailView

urlpatterns = [
    path("", ProfessorListView.as_view(), name="professor-list"),
    path("<int:pk>/", ProfessorDetailView.as_view(), name="professor-detail"),
]
