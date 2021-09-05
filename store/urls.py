from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.shop, name='shop'),
    path('product_details', views.product_details, name='product_details'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart'),
]
