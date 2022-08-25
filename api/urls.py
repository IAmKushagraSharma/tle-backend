from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', endpoints),
    path('satname/<str:satname>/', byname),
    path('tlebyname/<str:satname>/', tlebyname),
    path('satid/<int:satid>/', byid),
    path('satellite/', views.satellite_list),
    path('satellite/<name>', views.satellite_detail),
    path('satellite/<name>/<sensor>', views.sensor_detail),
    path('sensor/', views.sensor_list),
    path('sensor/<name>', views.satellite_name),
    path('sensor/<name>/<sensor>', views.sensor_detail),
    path('application/', views.application_list),
    path('application/<applicationname>', views.application_to_sensor_details),

]
