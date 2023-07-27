from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sign_up_newsletter', views.sign_up_newsletter,
         name='sign_up_newsletter'),
    path('terms_conditions', views.terms_conditions, name='terms_conditions'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]
