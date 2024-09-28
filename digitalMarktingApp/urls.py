from django.urls import path
from digitalMarktingApp import views

urlpatterns = [
    path('', views.index, name="home"),
    
]
