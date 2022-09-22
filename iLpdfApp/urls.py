from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('merge_pdf', views.mergepdf, name= 'mergepdf'),
    path('desktop', views.devices, name= 'devices'),
]