from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sign_up_newsletter', views.sign_up_newsletter, name='sign_up_newsletter'),
]
