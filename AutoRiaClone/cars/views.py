from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Car

def home(request):
    cars = Car.objects.all()
    return render(request, "cars/home.html", {"cars": cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, "cars/car_detail.html", {"car": car})

def filter_cars(request):
    filtered = Car.objects.all()

    brand = request.GET.get("brand")
    year = request.GET.get("year")
    fuel = request.GET.get("fuel")
    transmission = request.GET.get("transmission")
    max_price = request.GET.get("max_price")

    if brand and brand != "all":
        filtered = filtered.filter(brand=brand)

    if year and year != "all":
        filtered = filtered.filter(year=int(year))

    if fuel and fuel != "all":
        filtered = filtered.filter(fuel=fuel)

    if transmission and transmission != "all":
        filtered = filtered.filter(transmission=transmission)

    if max_price and max_price != "all":
        filtered = filtered.filter(price__lte=int(max_price))

    cars_data = []
    for car in filtered:
        cars_data.append({
            'id': car.id,
            'brand': car.brand,
            'model': car.model,
            'price': car.price,
            'year': car.year,
            'mileage': car.mileage,
            'engine': car.engine,
            'region': car.region,
            'image': car.image.url if car.image else '/static/cars/img/placeholder.png',
        })

    return JsonResponse({"cars": cars_data})
