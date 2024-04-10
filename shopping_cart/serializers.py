from rest_framework import serializers
from .models import ShoppingCart, ShoppingCartItem

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = "__all__"

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    productid = serializers.ReadOnlyField(source="product.id")
    class Meta:
        model =  ShoppingCartItem
        fields = "__all__"