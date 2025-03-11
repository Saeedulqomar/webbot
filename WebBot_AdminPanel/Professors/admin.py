from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_info', 'linked_in', 'office_hours')  # Поля для отображения в списке
    search_fields = ('full_name', 'contact_info')  # Поиск по этим полям
    ordering = ('full_name',)  # Сортировка по имени

admin.site.register(Professor, ProfessorAdmin)
