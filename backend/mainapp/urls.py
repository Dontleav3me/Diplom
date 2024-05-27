from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('projects/', get_projects, name='get_projects'),
    path('directions/', get_directions, name='get_directions'),
    path('news/', get_news, name='get_news'),
    path('bottom_news/', get_bottom_news, name='get_bottom_news'),
    path('mini_news/', get_mini_news, name='get_mini_news'),
    path('solo_news/', get_solo_news, name='get_solo_news'),
]