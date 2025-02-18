from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('login/', views.LoginView.as_view(success_url=reverse_lazy('home:home')), name='login'),
    path("login/", auth_views.LoginView.as_view(template_name='home/login.html'), name="login"),
    path('register/', views.RegisterView.as_view(success_url=reverse_lazy('home:login')), name='register'),
]