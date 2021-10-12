from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='hm'),

    path('srch/', views.searching, name='search1'),
    path('<slug:c_slug>/srch', views.searching, name='search1'),
    # path('details/', views.prod_detail, name='details'),
    path('<slug:c_slug>/<slug:product_slug>',views.prd_detail, name='details'),

    path('<slug:c_slug>/',views.home,name='prod_cat'),
]
