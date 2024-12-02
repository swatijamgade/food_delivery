from django.urls import path
from .views import CartListView, CartDetailView, CartItemDetailView, MenuItemView, MenuItemDetailView

urlpatterns = [
    path('carts/', CartListView.as_view(), name='cart-item'),
    path('carts/<int:pk>/',CartDetailView.as_view(), name='cart-detail'),
    path('cart-items/', CartListView.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('menu-items/', MenuItemView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),

]