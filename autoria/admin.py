from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_usd', 'city', 'created_at')
    list_filter = ('transmission', 'body_type', 'city')
    search_fields = ('brand', 'model', 'city', 'plate', 'vin')
    readonly_fields = ('created_at', 'posted', 'price_uah')
