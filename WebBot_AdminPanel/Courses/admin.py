from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_type', 'professor', 'description')  # Поля для отображения в списке
    search_fields = ('course_name', 'course_type', 'professor__full_name')  # Поиск по этим полям
    list_filter = ('course_type', 'professor')  # Фильтрация по типу курса и профессору
    ordering = ('course_name', 'course_type')  # Сортировка по названию курса

admin.site.register(Course, CourseAdmin)
