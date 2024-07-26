from rest_framework import serializers
from .models import Order, OrderItem
from User.models import User
from Product.models import Product

# ORDERS LIST SERIALIZERS

class OrderListsUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class OrdersListSerializer(serializers.ModelSerializer):
    user = OrderListsUsernameSerializer()
    class Meta:
        model = Order
        exclude = ["id"]

# ORDERS LIST SERIALIZERS


# ORDERS DETAIL SERIALIZERS

# 1 - ORDER DETAIL

class OrdersOwnerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class OrderDetailSerializer(serializers.ModelSerializer):
    user = OrdersOwnerDetailSerializer()
    class Meta:
        model = Order
        exclude = ["id"]

# 2 - ORDER ITEMS DETAIL

class OrderItemsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "product_code"]

class OrderItemSerializer(serializers.ModelSerializer):
    product = OrderItemsProductSerializer()
    class Meta:
        model = OrderItem
        fields = ["product", "item_code"]

# ORDERS DETAIL SERIALIZERS


# UPDATE ORDERS SERIALIZERS

class UpdateOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["is_verified"]

# UPDATE ORDERS SERIALIZERS
