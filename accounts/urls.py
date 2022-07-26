from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register ,name = 'register'),
    path('login/', views.login_, name ='login'),
    path('dashboard/', views.dash, name ='dashboard'),
    path('logout/', views.logout_ ,name='logout')
]