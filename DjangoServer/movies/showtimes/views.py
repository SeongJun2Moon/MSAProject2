from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from movies.showtimes.repositories import ShowtimesRepository
from movies.showtimes.serializers import ShowtimesSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def showtimes(request):
    if request.method == "POST":
        return ShowtimesSerializer().create(request.data)
    elif request.method == "GET":
        return ShowtimesSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return ShowtimesSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ShowtimesSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def showtimes_list(request):  return ShowtimesRepository().get_all(request.data)