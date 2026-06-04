from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'fuel', 'transmission', 'image_preview')
    list_filter = ('brand', 'year', 'fuel', 'transmission')
    search_fields = ('brand', 'model', 'region')
    ordering = ('-created_at',)

    fieldsets = (
        ('Основна інформація', {
            'fields': ('brand', 'model', 'year', 'price')
        }),
        ('Характеристики', {
            'fields': ('fuel', 'transmission', 'engine', 'mileage', 'region')
        }),
        ('Фотографія', {
            'fields': ('image',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return '✓'
        return '✗'
    image_preview.short_description = 'Фото'
