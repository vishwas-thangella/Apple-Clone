from django.db import models

# Create your models here.

class DeviceCoverage(models.Model):
    serial = models.CharField(max_length=180)

class Categories(models.Model):
    name = models.CharField(max_length=200)
    img = models.URLField()

class Device(models.Model):
    name = models.CharField(max_length=300)
    img = models.CharField(max_length=300)
    desc = models.TextField(max_length=500)
    price = models.IntegerField()
    model = models.CharField(max_length=10)