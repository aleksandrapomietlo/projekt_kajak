from django.db import models
from datetime import datetime

class Route(models.Model):
    '''Stores information details about available routes'''
    name = models.CharField(max_length=128)
    content = models.TextField()
    route_map = models.ImageField(upload_to='routes')


SEAT_NUMBER = (
    (1, "jednoosobowy"),
    (2, "dwuosobowy"),
    (3, "rodzinny"),
)

class Kayak(models.Model):
    '''Stores information details about kayak models'''
    name = models.CharField(max_length=128)
    content = models.TextField()
    seats = models.IntegerField(choices=SEAT_NUMBER)
    kayak_image = models.ImageField(upload_to='images')

class Message(models.Model):
    '''Stores message contents'''
    text = models.TextField()

class Reservation(models.Model):
    '''Stores reservation details, related to: :model: 'kajak.Route',
     :model: 'kajak.Kayak', :model: 'kajak.Message'.'''
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    participants = models.IntegerField()
    kayaks = models.ManyToManyField(Kayak)
    phone_number = models.CharField(max_length=12)
    payment = models.BooleanField()
    mail = models.EmailField(max_length=128)
    message = models.OneToOneField(Message, on_delete=models.CASCADE)


class Planned(models.Model):
    '''Stores information about planned events, related to: :model: 'kajak.Route'.
    '''
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()

