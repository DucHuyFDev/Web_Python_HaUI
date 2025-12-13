from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='service'),
    path('help/', views.help, name='help'),
]
