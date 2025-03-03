from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  # Поля для отображения в списке
    search_fields = ('question',)  # Поиск по вопросу
    list_filter = ('question',)  # Фильтрация по вопросу

admin.site.register(Question, QuestionAdmin)
