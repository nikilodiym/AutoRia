from django.db import models

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('A', 'Automatic'),
        ('M', 'Manual'),
    ]

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()

    price_usd = models.PositiveIntegerField()
    price_uah = models.PositiveIntegerField()

    mileage = models.PositiveIntegerField()
    transmission = models.CharField(max_length=1, choices=TRANSMISSION_CHOICES)

    engine = models.CharField(max_length=50)
    city = models.CharField(max_length=100, default="Unknown")

    plate = models.CharField(max_length=20)
    posted = models.CharField(max_length=50)

    image = models.URLField() # або ImageField якщл захочу файли вставляти

    def __str__(self):
        return f"{self.brand} {self.model}"