from django.db import models

class project(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)