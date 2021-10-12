from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('addCart/<int:product_id>/',views.add_cart,name='addcrt'),
    path('cart_decrement/<int:product_id>/', views.min_cart, name='cartMin'),
    path('remove/<int:product_id>/', views.cart_delete, name='remove'),

]
