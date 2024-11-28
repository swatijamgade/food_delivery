from rest_framework import serializers
from .models import Cart, CartItem, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = MenuItem
        fields = ['id', 'name', 'price', 'description']

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    class Meta:
        models = CartItem
        fields = ['id', 'menu_item','quentity']


class CartSerializer(serializers.ModelSerializer):
    item = CartItemSerializer(many=True)

    class Meta:
        models = Cart
        fields = ['id','user', 'item', 'created_at', 'updated_at']


