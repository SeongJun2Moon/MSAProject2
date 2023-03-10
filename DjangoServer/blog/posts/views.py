from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from blog.posts.repositories import PostsRepository
from blog.posts.serializers import PostsSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def posts(request):
    if request.method == "POST":
        return PostsSerializer().create(request.data)
    elif request.method == "GET":
        return PostsSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return PostsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return PostsSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def posts_list(request):  return PostsRepository().get_all(request.data)