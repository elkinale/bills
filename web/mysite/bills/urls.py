from django.urls import path, include
from . import views


app_name = 'bills'
urlpatterns = [
    path('main/', views.MainView.as_view(), name='main'),
    path('bills/create', views.AddBillView.as_view(), name='bill_create'),
    path('bills/<int:pk>/detail', views.DetailBillView.as_view(), name='bill_detail'),
    path('bills/<int:pk>/update', views.UpdateBillView.as_view(), name='bill_update'),
    path('bills/<int:pk>/delete', views.DeleteBillView.as_view(), name='bill_delete'), 
    path('event-autocomplete/', views.EventAutocomplete.as_view(), name='event_autocomplete')
]  
