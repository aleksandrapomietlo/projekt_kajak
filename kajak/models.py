from django.db import models
from datetime import datetime

class Route(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField()
    route_map = models.ImageField(upload_to='routes')


SEAT_NUMBER = (
    (1, "jednoosobowy"),
    (2, "dwuosobowy"),
    (3, "rodzinny"),
)

class Kayak(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField()
    seats = models.IntegerField(choices=SEAT_NUMBER)
    kayak_image = models.ImageField(upload_to='images')

class Form(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    participants = models.IntegerField()
    kayaks = models.ManyToManyField(Kayak)
    phone_number = models.CharField(max_length=12)
    payment = models.BooleanField()
    mail = models.EmailField(max_length=128)


class planned(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()

class message(models.Model):
    text = models.TextField()