from django.contrib import admin
from .models import Event, Organizer

class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Поля для отображения в списке
    search_fields = ('name',)  # Поиск по имени
    list_filter = ('name',)  # Фильтрация по имени

admin.site.register(Organizer, OrganizerAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'organized_by', 'venue')  # Поля для отображения в списке
    search_fields = ('name', 'venue', 'organized_by__name')  # Поиск по этим полям
    list_filter = ('date', 'organized_by')  # Фильтрация по типу события, дате и организатору
    ordering = ['date']  # Сортировка по дате и типу события

admin.site.register(Event, EventAdmin)
