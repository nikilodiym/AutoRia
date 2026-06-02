from django.shortcuts import render
from .car_data import cars
from django.http import JsonResponse

def home(request):
    return render(
        request,
        "cars/home.html",
        {
            "cars": cars
        }
    )

def car_detail(request, car_id):

    selected_car = None

    for car in cars:

        if car["id"] == car_id:

            selected_car = car
            break

    return render(
        request,
        "cars/car_detail.html",
        {
            "car": selected_car
        }
    )

# def search_cars(request):
#     query = request.GET.get("q", "").lower()
#
#     results = []
#
#     for car in cars:
#         if query in car["brand"].lower() or query in car["model"].lower():
#             results.append(car)
#
#     return JsonResponse({"cars": results})

def filter_cars(request):
    filtered = cars

    brand = request.GET.get("brand")
    year = request.GET.get("year")
    fuel = request.GET.get("fuel")
    transmission = request.GET.get("transmission")
    max_price = request.GET.get("max_price")

    if brand and brand != "all":
        filtered = [c for c in filtered if c["brand"] == brand]

    if year and year != "all":
        filtered = [c for c in filtered if str(c["year"]) == year]

    if fuel and fuel != "all":
        filtered = [c for c in filtered if c["fuel"] == fuel]

    if transmission and transmission != "all":
        filtered = [c for c in filtered if c["transmission"] == transmission]

    if max_price and max_price != "all":
        filtered = [c for c in filtered if c["price"] <= int(max_price)]

    return JsonResponse({"cars": filtered})