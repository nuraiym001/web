from django.urls import path

from api.views import *

urlpatterns = [
    path('products/', products_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:categories_id>/products/', category_products),
]