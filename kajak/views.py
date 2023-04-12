from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
def routes(request):
    return render(request, "routes.html")
def kayaks(request):
    return render(request, "kayaks.html")
def reservation(request):
    return render(request, "reservation.html")
def gallery(request):
    return render(request, "gallery.html")
def login(request):
    return render(request, "login.html")
def register(request):
    return render(request, "register.html")
def upcoming(request):
    return render(request, "upcoming.html")
