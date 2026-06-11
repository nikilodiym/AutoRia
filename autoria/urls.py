from django.urls import path

from .views import car_detail, index, login, sell_car

urlpatterns = [
    path('', index, name='index'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
    path('sell/', sell_car, name='sell_car'),
    path('login/', login, name='login'),
]
