from django.contrib import admin
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = (
        'name',
        'category',
        'price',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'review',
        'rating',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Category, CategoryAdmin)
