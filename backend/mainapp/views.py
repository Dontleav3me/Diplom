from django.shortcuts import render
from mainapp.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import project, Directions, News, BottomNews, MiniNew, SoloNews
from .serializers import (
    ProjectSerializer, DirectionsSerializer, NewsSerializer, 
    BottomNewsSerializer, MiniNewSerializer, SoloNewsSerializer, NewsTopSerializer
)
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@api_view(['GET'])
def get_projects(request):
    projects = project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def get_directions(request):
    directions = Directions.objects.all()
    serializer = DirectionsSerializer(directions, many=True)
    return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def get_bottom_news(request):
    bottom_news = BottomNews.objects.all()
    serializer = BottomNewsSerializer(bottom_news, many=True)
    return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def get_mini_news(request):
    mini_news = MiniNew.objects.all()
    serializer = MiniNewSerializer(mini_news, many=True)
    return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def get_solo_news(request):
    solo_news = SoloNews.objects.all()
    serializer = SoloNewsSerializer(solo_news, many=True)
    return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def get_newstop(request):
    solo_news = NewsTop.objects.all()
    serializer = NewsTopSerializer(solo_news, many=True)
    return Response(serializer.data)
