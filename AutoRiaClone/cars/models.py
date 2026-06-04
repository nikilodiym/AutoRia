from django.db import models
from django.utils import timezone

class Car(models.Model):
    FUEL_CHOICES = [
        ('Бензин', 'Бензин'),
        ('Дизель', 'Дизель'),
        ('Електро', 'Електро'),
    ]

    TRANSMISSION_CHOICES = [
        ('Автомат', 'Автомат'),
        ('Мкпп', 'Мкпп'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    mileage = models.IntegerField(default=0)
    engine = models.CharField(max_length=100, default="N/A")
    region = models.CharField(max_length=100, default="N/A")
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES, default='Бензин')
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, default='Автомат')
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
