
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listing' ),
    path('<int:listing_id>/list', views.list, name ='list'),
    path('search', views.search, name ='search'),
    # path('inquery', views.inquiry, name ='inquiry')
]