from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarForm, LoginForm, RegisterForm
from .models import Car, Favorite


def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser, login_url='login')(view_func)


def get_favorite_car_ids(request):
    if not request.user.is_authenticated:
        return set()
    return set(Favorite.objects.filter(user=request.user).values_list('car_id', flat=True))


def filter_cars(request, cars):
    filters = {
        'condition': request.GET.get('condition', 'all'),
        'type': request.GET.get('type', ''),
        'brand': request.GET.get('brand', ''),
        'year_from': request.GET.get('year_from', ''),
        'year_to': request.GET.get('year_to', ''),
        'price_from': request.GET.get('price_from', ''),
        'price_to': request.GET.get('price_to', ''),
        'regions': request.GET.getlist('region'),
        'fuels': request.GET.getlist('fuel'),
        'transmissions': request.GET.getlist('transmission'),
        'models': request.GET.getlist('model'),
    }

    if filters['condition'] == 'used':
        cars = cars.filter(year__lt=2024)
    elif filters['condition'] == 'new':
        cars = cars.filter(year__gte=2024)

    if filters['brand']:
        cars = cars.filter(brand__iexact=filters['brand'])

    if filters['models']:
        model_query = Q()
        for model in filters['models']:
            model_query |= Q(model__iexact=model)
        cars = cars.filter(model_query)

    if filters['year_from'].isdigit():
        cars = cars.filter(year__gte=int(filters['year_from']))

    if filters['year_to'].isdigit():
        cars = cars.filter(year__lte=int(filters['year_to']))

    if filters['price_from'].isdigit():
        cars = cars.filter(price_usd__gte=int(filters['price_from']))

    if filters['price_to'].isdigit():
        cars = cars.filter(price_usd__lte=int(filters['price_to']))

    region_names = {
        'kyiv': ['Київ', 'Київська'],
        'zhytomyr': ['Житомир', 'Житомирська'],
        'sumy': ['Суми', 'Сумська'],
        'chernihiv': ['Чернігів', 'Чернігівська'],
        'vinnytsia': ['Вінниця', 'Вінницька'],
        'poltava': ['Полтава', 'Полтавська'],
        'cherkasy': ['Черкаси', 'Черкаська'],
        'lviv': ['Львів', 'Львівська'],
        'ivano': ['Івано-Франківськ', 'Івано-Франківська'],
        'odesa': ['Одеса', 'Одеська'],
        'kherson': ['Херсон', 'Херсонська'],
    }
    if filters['regions']:
        region_query = Q()
        for region in filters['regions']:
            for label in region_names.get(region, []):
                region_query |= Q(region__icontains=label) | Q(city__icontains=label)
        if region_query:
            cars = cars.filter(region_query)

    fuel_words = {
        'gasoline': ['бензин', 'gasoline'],
        'diesel': ['дизель', 'diesel'],
        'gas': ['газ'],
        'electric': ['електро', 'electric'],
        'hybrid': ['гібрид', 'hybrid'],
        'gas_gasoline': ['газ', 'бензин'],
    }
    if filters['fuels']:
        fuel_query = Q()
        for fuel in filters['fuels']:
            for word in fuel_words.get(fuel, []):
                fuel_query |= Q(engine__icontains=word)
        if fuel_query:
            cars = cars.filter(fuel_query)

    transmission_codes = {
        'manual': 'M',
        'auto': 'A',
        'tiptronic': 'A',
        'robot': 'A',
        'variator': 'A',
        'reductor': 'A',
    }
    transmission_values = [transmission_codes[value] for value in filters['transmissions'] if value in transmission_codes]
    if transmission_values:
        cars = cars.filter(transmission__in=transmission_values)

    return cars.distinct(), filters


def index(request):
    cars, filters = filter_cars(request, Car.objects.all())
    return render(request, 'index/index.html', {
        'cars': cars,
        'filters': filters,
        'favorite_car_ids': get_favorite_car_ids(request),
    })


def used_cars(request):
    cars = Car.objects.filter(year__lt=2024)
    if not cars.exists():
        cars = Car.objects.all()
    return render(request, 'used_cars/used_cars.html', {
        'cars': cars,
        'favorite_car_ids': get_favorite_car_ids(request),
    })


def new_cars(request):
    cars = Car.objects.filter(year__gte=2024)
    if not cars.exists():
        cars = Car.objects.all()[:3]
    return render(request, 'new_cars/new_cars.html', {
        'cars': cars,
        'favorite_car_ids': get_favorite_car_ids(request),
    })


def car_services(request):
    return render(request, 'car_services/car_services.html')


@login_required
def garage(request):
    return render(request, 'garage/garage.html')


def support(request):
    return render(request, 'support/support.html')


def search(request):
    cars = Car.objects.all()
    return render(request, 'search/search.html', {
        'cars': cars,
        'favorite_car_ids': get_favorite_car_ids(request),
    })


@login_required
def favorites(request):
    cars = Car.objects.filter(favorited_by__user=request.user)
    return render(request, 'favorites/favorites.html', {
        'cars': cars,
        'favorite_car_ids': get_favorite_car_ids(request),
    })


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    similar_cars = Car.objects.exclude(pk=car.pk)[:6]
    return render(request, 'car_detail/car_detail.html', {
        'car': car,
        'similar_cars': similar_cars,
        'favorite_car_ids': get_favorite_car_ids(request),
    })


@login_required
def toggle_favorite(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, car=car)
    if created:
        messages.success(request, f'{car.brand} {car.model} додано в обране.')
    else:
        favorite.delete()
        messages.success(request, f'{car.brand} {car.model} прибрано з обраного.')
    return redirect(request.POST.get('next') or 'favorites')


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
