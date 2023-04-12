from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Konto założone dla {username}. Możesz się zalogować")
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
# Create your views here.
