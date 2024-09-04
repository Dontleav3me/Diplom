from django.shortcuts import render
from mainapp.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import project, Directions, BottomNews, MiniNew, SoloNews
from .serializers import (
    ProjectSerializer, DirectionsSerializer,
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
@api_view(['GET'])
def get_item(request):
    user_id = request.query_params.get('user_id')
    #user = TelegramUser.objects.get(user_id = user_id)
    #serializer = TelegramUserSerializer(user)
    #return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("")
@csrf_exempt
@api_view(['GET'])
def get_bottom_news_detail(request, id):
    try:
        news_item = BottomNews.objects.get(id=id)
        serializer = BottomNewsSerializer(news_item)
        return Response(serializer.data)
    except BottomNews.DoesNotExist:
        return Response(status=404, data={'message': 'BottomNews not found'})

@csrf_exempt
@api_view(['GET'])
def get_news_top_detail(request, id):
    try:
        news_item = NewsTop.objects.get(id=id)
        serializer = NewsTopSerializer(news_item)
        return Response(serializer.data)
    except NewsTop.DoesNotExist:
        return Response(status=404, data={'message': 'NewsTop not found'})
@csrf_exempt
@api_view(['GET'])
def get_project_detail(request, id):
    try:
        proj = project.objects.get(id=id)
        serializer = ProjectSerializer(proj)
        return Response(serializer.data)
    except project.DoesNotExist:
        return Response(status=404, data={'message': 'Project not found'})