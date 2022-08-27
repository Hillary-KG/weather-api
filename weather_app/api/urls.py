from django.urls import path
from . import views


urlpatterns = [
    path('api/locations/<str:city>/', views.get_weather_forcast, name='get-weather-data')
]
