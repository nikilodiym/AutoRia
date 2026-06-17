from django.urls import path

from .views import (
    car_detail,
    car_services,
    favorites,
    garage,
    index,
    login,
    logout,
    new_cars,
    register,
    search,
    sell_car,
    support,
    used_cars,
)

urlpatterns = [
    path('', index, name='index'),
    path('used-cars/', used_cars, name='used_cars'),
    path('new-cars/', new_cars, name='new_cars'),
    path('car-services/', car_services, name='car_services'),
    path('garage/', garage, name='garage'),
    path('support/', support, name='support'),
    path('search/', search, name='search'),
    path('favorites/', favorites, name='favorites'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
    path('sell/', sell_car, name='sell_car'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
