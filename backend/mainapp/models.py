from django.db import models
from django.contrib import admin
class project(models.Model):
    name = models.CharField(max_length=256)
    subname = models.CharField(max_length=1024)

class Directions(models.Model):
    name = models.CharField(max_length=256)
    subname = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/')

class BottomNews(models.Model):
    name = models.CharField(max_length=256)
    subname = models.CharField(max_length=256)
    time = models.CharField(max_length=256)
    dela = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/')

class MiniNew(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=256)

class SoloNews(models.Model):
    name = models.CharField(max_length=256)
    subname = models.CharField(max_length=256)
    dela = models.CharField(max_length=256)
    geo = models.CharField(max_length=256)
    date = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/')
    head = models.CharField(max_length=256)
    header_items = models.CharField(max_length=256)
    name_items = models.CharField(max_length=256)
    subname_items = models.CharField(max_length=256)
    img_mobile = models.ImageField(upload_to='images/')
    img_items = models.ImageField(upload_to='images/')

    
class NewsTop(models.Model):
    image = models.ImageField(upload_to='images/')
    head = models.CharField(max_length=256)
    date = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    dela = models.CharField(max_length=512)
    time = models.CharField(max_length=256)

admin.site.register(project)
admin.site.register(Directions)
admin.site.register(BottomNews)
admin.site.register(MiniNew)
admin.site.register(SoloNews)
admin.site.register(NewsTop)