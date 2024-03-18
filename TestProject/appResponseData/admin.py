from django.contrib import admin
from .models import GenerateData, GenerateTab


@admin.register(GenerateTab)
class GenerateTabAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'status']
    list_display_links = ['number']
    list_filter = ['status']
    list_per_page = 20
    search_field = ['number']
    ordering = ['number']
    list_editable = ['status']


@admin.register(GenerateData)
class GenerateDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'status']
    list_display_links = ['date_time']
    list_filter = ['status', 'date_time']
    list_per_page = 20
    search_field = ['date_time']
    readonly_fields = ['date_time']
    ordering = ['-date_time']
    list_editable = ['status']