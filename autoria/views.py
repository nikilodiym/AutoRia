from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarForm, LoginForm, RegisterForm
from .models import Car


def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser, login_url='login')(view_func)


def index(request):
    cars = Car.objects.all()
    return render(request, 'index/index.html', {'cars': cars})


def used_cars(request):
    cars = Car.objects.filter(year__lt=2024)
    if not cars.exists():
        cars = Car.objects.all()
    return render(request, 'used_cars/used_cars.html', {'cars': cars})


def new_cars(request):
    cars = Car.objects.filter(year__gte=2024)
    if not cars.exists():
        cars = Car.objects.all()[:3]
    return render(request, 'new_cars/new_cars.html', {'cars': cars})


def car_services(request):
    return render(request, 'car_services/car_services.html')


@login_required
def garage(request):
    return render(request, 'garage/garage.html')


def support(request):
    return render(request, 'support/support.html')


def search(request):
    cars = Car.objects.all()
    return render(request, 'search/search.html', {'cars': cars})


@login_required
def favorites(request):
    cars = Car.objects.all()[:3]
    return render(request, 'favorites/favorites.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    similar_cars = Car.objects.exclude(pk=car.pk)[:6]
    return render(request, 'car_detail/car_detail.html', {
        'car': car,
        'similar_cars': similar_cars,
    })


@login_required
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


@superuser_required
def admin_cars(request):
    cars = Car.objects.all()
    return render(request, 'admin_cars/admin_cars.html', {'cars': cars})


@superuser_required
def admin_car_edit(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save()
            messages.success(request, f'Оголошення {car.brand} {car.model} оновлено.')
            return redirect('admin_cars')
    else:
        form = CarForm(instance=car)

    return render(request, 'sell/sell.html', {
        'form': form,
        'page_title': 'Редагувати авто',
        'page_subtitle': 'Оновіть дані оголошення. Зміни одразу відобразяться на сайті.',
        'submit_label': 'Зберегти зміни',
        'cancel_url': 'admin_cars',
    })


@superuser_required
def admin_car_delete(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        car_name = f'{car.brand} {car.model} {car.year}'
        car.delete()
        messages.success(request, f'Оголошення {car_name} видалено.')
        return redirect('admin_cars')

    return render(request, 'admin_cars/admin_car_delete.html', {'car': car})


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_login(request, form.get_user())
        messages.success(request, 'Ви успішно увійшли в кабінет.')
        return redirect(request.GET.get('next') or 'index')

    return render(request, 'login/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        auth_login(request, user)
        messages.success(request, 'Акаунт створено. Вітаємо на AUTO.RIA!')
        return redirect('index')

    return render(request, 'register/register.html', {'form': form})


def logout(request):
    auth_logout(request)
    messages.success(request, 'Ви вийшли з акаунта.')
    return redirect('index')
