from django.db import models
from django.contrib import admin
class project(models.Model):
    name = models.CharField(max_length=256)
    subname = models.CharField(max_length=1024)

class Directions(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/')

class News(models.Model):
    head = models.CharField(max_length=128)
    date = models.CharField(max_length=25)
    name = models.CharField(max_length=200)
    dela = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

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
    image = models.ImageField(max_length=256)
    head = models.CharField(max_length=256)


class NewsTop(models.Model):
    image = models.ImageField(upload_to='images/')
    head = models.CharField(max_length=256)
    date = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    dela = models.CharField(max_length=512)
    time = models.CharField(max_length=256)

admin.site.register(project)
admin.site.register(Directions)
admin.site.register(News)
admin.site.register(BottomNews)
admin.site.register(MiniNew)
admin.site.register(SoloNews)
admin.site.register(NewsTop)