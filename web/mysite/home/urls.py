from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("login/", views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name='register'),
]