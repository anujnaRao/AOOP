from django.contrib import admin
from django.urls import path
from empApp import views
from empApp.views import HomePage, DisplayPage

urlpatterns = [
    path('', HomePage.as_view()),
    path('display/', DisplayPage.as_view(), name='display'),
]
