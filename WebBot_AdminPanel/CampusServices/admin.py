from django.contrib import admin
from .models import CampusService

class CampusServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'short_description')
    search_fields = ('name', 'contact')
    ordering = ('name',)
    list_per_page = 20  # Pagination in admin
    fieldsets = (
        ("Basic Information", {
            'fields': ('name', 'description')
        }),
        ("Contact Details", {
            'fields': ('contact',),
            'classes': ('collapse',)  # Hides section by default
        }),
    )

    def short_description(self, obj):
        return obj.description[:50] + "..." if obj.description else "No description"
    short_description.short_description = "Short Description"

# ✅ Registering the model with the custom admin panel
admin.site.register(CampusService, CampusServiceAdmin)
