from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('student-form/', views.student_form_view, name="student-form"),
]
