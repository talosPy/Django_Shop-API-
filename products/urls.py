from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('<int:id>/', views.product_detail, name="product_detail"),
    path('categories/', views.category_list, name="category_list"),  # Add this line
    path('categories/<int:id>/', views.category_detail, name="category_detail"),  # Add this line


]
