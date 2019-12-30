from django.contrib import admin
from django.urls import path
from empApp import views

urlpatterns = [
    path(' ', views.HomePage.as_view(), name='home'),
    path('display/', views.DisplayPage.as_view(), name='display'),
]
