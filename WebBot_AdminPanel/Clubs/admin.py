from django.contrib import admin
from .models import Club

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')  # Поля для отображения в списке
    search_fields = ('name', 'link')  # Поиск по имени и ссылке
    list_filter = ('name',)  # Фильтрация по имени

admin.site.register(Club, ClubAdmin)
