from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('bookings', views.bookings, name='bookings'),
    path('reservation_success', views.reservation_success,
         name='reservation_success'),
]
