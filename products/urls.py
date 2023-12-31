from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='menu'),
    path('<int:product_id>/', views.menu_item, name='menu_item'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('ajax_add_review/<int:product_id>/', views.ajax_add_review,
         name='ajax_add_review'),
]
