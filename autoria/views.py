from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarForm
from .models import Car


def index(request):
    cars = Car.objects.all()
    return render(request, 'index/index.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    similar_cars = Car.objects.exclude(pk=car.pk)[:6]
    return render(request, 'car_detail/car_detail.html', {
        'car': car,
        'similar_cars': similar_cars,
    })


def sell_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            messages.success(
                request,
                f'Оголошення {car.brand} {car.model} {car.year} успішно опубліковано!',
            )
            return redirect('index')
    else:
        form = CarForm()

    return render(request, 'sell/sell.html', {'form': form})


def login(request):
    return render(request, 'login/login.html')
