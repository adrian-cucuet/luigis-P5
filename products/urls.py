from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='menu'),
    path('<product_id>', views.menu_item, name='menu_item'),
]
