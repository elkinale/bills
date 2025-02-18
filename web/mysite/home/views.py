from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.conf import settings
# from django.contrib.auth import login
from .forms import RegistrationForm

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
    success_url = 'home:home'
    def get(self, request):
        return render(request, 'home/login.html')
    
    def post(self, request):
        context = request
        return redirect(self.success_url)
    
class RegisterView(View):
    success_url = reverse_lazy('home:login')
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'home/register.html', {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user) # Log the user in after registration
            return redirect(self.success_url)
        else:
            return render(request, 'home/register.html', {'form':form})
    
