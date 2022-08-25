from django.urls import path
from .views import *

urlpatterns = [
    path('', endpoints),
    path('satname/<str:satname>/', byname),
    path('tlebyname/<str:satname>/', tlebyname),
    path('satid/<int:satid>/', byid),
]
