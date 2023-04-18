from django import forms
from models import Form
class ReservationForm(forms.ModelForm):
    model = Form
    fields = ('name', 'surname', 'mail', 'phone_number', 'route', 'date', 'participants', 'kayaks', 'payment')