from django.urls import path
from product.views import ProductListView, ProductDetailView


urlpatterns = [
    path('products_list/', ProductListView.as_view(), name='products_list'),
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
]
