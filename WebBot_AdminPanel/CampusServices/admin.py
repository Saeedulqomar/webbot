from django.contrib import admin
from django.utils.html import format_html

from .models import Service, CampusService

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для отображения в списке
    search_fields = ('name',)  # Поиск по имени

admin.site.register(Service, ServiceAdmin)

class CampusServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_service_type', 'description', 'contact')  # Add a method for 'service_type'

    def get_service_type(self, obj):
        return obj.service_type.name  # Assuming 'service_type' is a ForeignKey to 'Service'
    get_service_type.admin_order_field = 'service_type'  # Allow sorting by 'service_type'
    get_service_type.short_description = 'Service Type'  # Custom column header


    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected services have been marked as active.")

    def archive_services(self, request, queryset):
        queryset.update(is_archived=True)
        self.message_user(request, "Selected services have been archived.")

    mark_as_active.short_description = "Mark selected as active"
    archive_services.short_description = "Archive selected services"

    def service_status(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green;">Active</span>')
        else:
            return format_html('<span style="color: red;">Inactive</span>')

    service_status.short_description = 'Status'

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Service Details', {
            'fields': ('service_type', 'contact'),
        }),
    )


admin.site.register(CampusService, CampusServiceAdmin)
