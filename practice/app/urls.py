from django.shortcuts import render
from django.urls import path
from .import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('all/', views.all, name='all'),
]
