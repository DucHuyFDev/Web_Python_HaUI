from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.student_form_view, name="signup"),
]
