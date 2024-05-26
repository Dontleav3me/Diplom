from django.db import models

class project(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

class Directions(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/')

class last_news(models.Model):
    