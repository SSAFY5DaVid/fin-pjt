from django.shortcuts import render, get_list_or_404
from .models import Post
from django.http import JsonResponse, HttpResponse
from django.core import serializers 

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication 





@api_view(['GET']) # response 쓸때 해당 decorator 필수
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommended(request):
    mode = request.GET.get('mode')
    key = 'popularity' if mode == 'popular' else 'release_date' if mode == 'latest' else 'vote_average'
    movies = Post.objects.order_by(f'-{key}')[:10]
    data = serializers.serialize('json', movies)
    return HttpResponse(data, content_type='application/json')
        

