from django.urls import path
from .views import user_cart_view, add_to_cart, all_carts_view

urlpatterns = [
    path('', all_carts_view, name='all_carts'),  # View all carts
    path('<str:username>/', user_cart_view, name='user_cart'),  # View cart by username
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),  # Add product to cart
]
