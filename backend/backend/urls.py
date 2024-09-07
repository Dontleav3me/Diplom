from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib import admin
from viewapp.views import *
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')), 
    re_path(r'^(?!admin|api/).*$', main),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)