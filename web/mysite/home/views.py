from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm

class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/main.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'home/login.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse_lazy('home:home'))
        
        return render(request, 'home/login.html', {'form':form})
    

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'home/register.html', {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user) # Log the user in after registration
            return redirect(reverse_lazy('home:login'))

        return render(request, 'home/register.html', {'form':form})
    
