from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', endpoints),
    path('tlebyname/<str:name>/', tle_by_name),
    path('tlebyid/<int:id>/', tle_by_id),
    path('satellite/', views.satellite_list),
    path('satellite/<name>', views.satellite_detail),
    path('satellite/<name>/<sensor>', views.sensor_detail),
    path('sensor/', views.sensor_list),
    path('sensor/<name>', views.satellite_name),
    path('sensor/<name>/<sensor>', views.sensor_detail),
    path('application/', views.application_list),
    path('application/<applicationname>', views.application_to_sensor_details),
    path('orbital_elements/<str:name>/', views.orbital_elements),
]   
