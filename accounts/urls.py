from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.reg, name='rg'),

    path('login',views.log,name='lg'),

    path('logout', views.logout, name='logout'),

]
