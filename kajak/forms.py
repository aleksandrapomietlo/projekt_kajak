from django import forms
from django.forms  import ModelForm
from .models import Reservation
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"#('route', 'date', 'name', 'surname', 'participants', 'kayaks', 'phone_number','payment', 'mail', 'message')