from django.contrib import admin
from .models import Temperature


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'temp', 'collected_at', 'created_at', 'updated_at')
    list_filter = ('collected_at', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
