from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path("search/", views.search_cars, name="search_cars"),
    path("filter/", views.filter_cars, name="filter_cars"),
    path('car/<int:car_id>/',views.car_detail,name='car_detail'),
]