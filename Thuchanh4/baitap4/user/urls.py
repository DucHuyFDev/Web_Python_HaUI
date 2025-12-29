from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('user-form/', views.user_form_view, name="user-form/"),
]