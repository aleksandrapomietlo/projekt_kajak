from .forms import ReservationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
def routes(request):
    return render(request, "routes.html")
def kayaks(request):
    return render(request, "kayaks.html")

def reservation(request):
    submitted = False
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reservation?submitted=True')
    else:
        form = ReservationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "reservation.html", {'form':form, 'submitted':submitted})

#class Reservation(TemplateView):
    #def get(self, request):
     ##  return render(request, 'reservation.html', {'form': form})
    #def post(self, request, res_id):
     #   p = ReservationForm.objects.get(pk=res_id)
      #  f = ReservationForm(request.POST, instance=p)
       ##    f.save()
         #   return render(request, "home.html")

def gallery(request):
    return render(request, "gallery.html")
def login(request):
    return render(request, "login.html")
def register(request):
    return render(request, "register.html")
def upcoming(request):
    return render(request, "upcoming.html")
