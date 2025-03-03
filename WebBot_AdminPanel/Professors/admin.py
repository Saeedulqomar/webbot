from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_info', 'course', 'linked_in', 'office_hours')  # Поля для отображения в списке
    search_fields = ('full_name', 'course', 'contact_info')  # Поиск по этим полям
    list_filter = ('course',)  # Фильтрация по курсу
    ordering = ('full_name',)  # Сортировка по имени

admin.site.register(Professor, ProfessorAdmin)
