from django.contrib import admin
from django.urls import path
from empApp import views
from empApp.views import HomePage, InsertPage

urlpatterns = [
    path('', HomePage.as_view(),name='home'),
    path('insert/', InsertPage.as_view(), name='insert'),
    path('show/', views.show, name='show')
]
