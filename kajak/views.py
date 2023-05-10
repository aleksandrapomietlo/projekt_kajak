from .forms import ReservationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View

class home(View):
    '''View checking whether user is logged in or not'''
    def get(self, request):
        current_user = request.user
        context = {'current:user': current_user}
        return render(request, "home.html", context)

def about(request):
    '''View displaying the about section of the website'''
    return render(request, "about.html")
def routes(request):
    '''View displaying the available routes with description'''
    return render(request, "routes.html")
def kayaks(request):
    '''View displaying tha available kayaks with description'''
    return render(request, "kayaks.html")

def reservation(request):
    '''Creates a new reservation and saves it to the database'''
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

def gallery(request):
    '''View displaying a gallery with photos from the events'''
    return render(request, "gallery.html")
def login(request):
    '''View displaying the login page'''
    return render(request, "login.html")
def register(request):
    '''View displaying the registration page'''
    return render(request, "register.html")
def upcoming(request):
    '''View displaying upcoming events for logged in users'''
    return render(request, "upcoming.html")
