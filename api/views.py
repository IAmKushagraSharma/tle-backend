import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

