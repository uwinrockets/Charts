from django.contrib import admin
from . import views
from django.urls import path

from .views import  HomeView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
]
