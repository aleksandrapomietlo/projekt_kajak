from django.db import models
from datetime import datetime

class Route(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField()
    route_map = models.ImageField(upload_to='/routes')

class Kayak(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField()
    kayak_image = models.ImageField(upload_to='/images')

class Form(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    participants = models.IntegerField()
    kayak_number = models.IntegerField()
    phone_number = models.CharField(max_length=12)
    payment = models.BooleanField()
    mail = models.EmailField(max_length=128)


class planned(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()

class message(models.Model):
    text = models.TextField()