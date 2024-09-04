from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('projects/', get_projects, name='get_projects'),
    path('directions/', get_directions, name='get_directions'),
    path('bottom_news/', get_bottom_news, name='get_bottom_news'),
    path('mini_news/', get_mini_news, name='get_mini_news'),
    path('solo_news/', get_solo_news, name='get_solo_news'),
    path('news_top/',get_newstop, name='get_solo_news'),
    path('get_item/',get_item, name='items'),
    path('bottom_news_detail/<int:id>/', get_bottom_news_detail, name='get_bottom_news_detail'),
    path('news_top_detail/<int:id>/', get_news_top_detail, name='get_news_top_detail'),
    path('project_detail/<int:id>/', get_project_detail, name='get_project_detail'),
]