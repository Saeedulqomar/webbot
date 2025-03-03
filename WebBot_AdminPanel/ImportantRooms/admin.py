from django.contrib import admin
from .models import BuildingName

class BuildingNameAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для отображения в списке
    search_fields = ('name',)  # Поиск по имени

admin.site.register(BuildingName, BuildingNameAdmin)

from django.contrib import admin
from .models import ImportantRoom

class ImportantRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'location', 'room_type', 'floor_number', 'building_name')  # Поля для отображения в списке
    search_fields = ('room_number', 'location', 'room_type', 'building_name__name')  # Поиск по этим полям
    list_filter = ('room_type', 'building_name')  # Фильтрация по типу комнаты и зданию
    ordering = ('building_name', 'floor_number', 'room_number')  # Сортировка по зданию и номеру комнаты

admin.site.register(ImportantRoom, ImportantRoomAdmin)

