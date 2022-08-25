import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from django.db.models import Q


@api_view(['GET'])
def endpoints(request):
    routes = [
        {
            'Endpoint': 'byname/<satellite name>',
            'method': 'GET',
            'body': None,
            'description': 'Returns TLE by it\'s name'
        },
        {
            'Endpoint': 'byid/<satellite id>',
            'method': 'GET',
            'body': None,
            'description': 'Returns TLE by it\'s id'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def byname(request, satname):
    response = requests.get(f'https://celestrak.org/NORAD/elements/gp.php?NAME={satname}&FORMAT=json').json()
    return Response(response)


@api_view(['GET'])
def tlebyname(request, satname):
    response = requests.get(f'https://celestrak.org/NORAD/elements/gp.php?NAME={satname}&FORMAT=TLE')
    return Response(response)


@api_view(['GET'])
def byid(request, satid):
    response = requests.get(f'https://celestrak.org/NORAD/elements/gp.php?CATNR={satid}&FORMAT=json').json()
    return Response(response)


@api_view(['GET'])
def orbital_elements(request, satName):
    data = requests.get(
        f'https://tle-backend.herokuapp.com/tlebyname/{satName}').json()

    tle_lines = [data["name"], data["line1"], data["line2"]]

    tle = TLE.from_lines(*tle_lines)
    orb = tle.to_orbit()

    Data = [
        {"semimajor_axis": orb.a},
        {"orbit_period": orb.period},
        {"eccentricity": orb.ecc},
        {"argument_of_perigree": orb.argp},
        {"inclination": orb.inc},
        {"mean_motion": orb.n},
        {"eccentricity_vector": orb.e_vec},
        {"true_anomaly": orb.nu},
        {"raan": orb.raan},
        {"epoch": orb.epoch},
        {"argument_of_latitude": orb.arglat},
    ]

    return Response(str(Data))


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def get_tle(request):
    response = requests.get(
        f'https://tle.ivanstanojevic.me/api/tle/?api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def tle_by_id(request, id):
    response = requests.get(
        f'https://tle.ivanstanojevic.me/api/tle/{id}?api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def tle_by_name(request, name):
    Id = SatNameId.objects.filter(Name=name)[0].SatId
    if (Id):
        response = requests.api.get(
            f'https://tle.ivanstanojevic.me/api/tle/{Id}?&api_key={api_key}').json()
    return Response(response)


@api_view(['GET'])
def satellite_list(request):
    if request.method == 'GET':
        satellite = SatelliteInfo.objects.all()
        serializer = SatelliteInfoSerializer(satellite, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def satellite_detail(request, name):
    try:
        satellite = SatelliteInfo.objects.get(pk=name)

    except satellite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sensor = Sensor.objects.filter(SatelliteName=satellite.Name)
        serializer = SensorSerializer(sensor, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def sensor_detail(request, name, sensor):
    if request.method == 'GET':
        sensor = Sensor.objects.filter(
            (Q(SatelliteName=name) & Q(SensorName=sensor)) | (Q(SensorName=name) & Q(SatelliteName=sensor)))
        serializer = SensorallSerializer(sensor, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def sensor_list(request):
    if request.method == 'GET':
        sensor = Sensor.objects.all()
        serializer = SensorSerializer(sensor, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def satellite_name(request, name):
    if request.method == 'GET':
        sensor = Sensor.objects.filter(SensorName=name)
        serializer = SatelliteNameSerializer(sensor, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def application_list(request):
    if request.method == 'GET':
        sensor = Sensor.objects.all()
        serializer = ApplicationSerializer(sensor, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def application_to_sensor_details(request, applicationname):
    if request.method == 'GET':
        sensor = Sensor.objects.filter(
            Q(application1=applicationname) | Q(application2=applicationname) | Q(application3=applicationname))
        serializer = SensorallSerializer(sensor, many=True)
        return Response(serializer.data)
