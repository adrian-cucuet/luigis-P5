from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    # path('reservation_create', views.reservation_create, name='reservation_create'),
    path('reservation_success', views.reservation_success, name='reservation_success'),
]
