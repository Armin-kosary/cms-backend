from rest_framework import serializers
from .models import Product

# PRODUCTS LIST SERIALIZERS

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id"]

# PRODUCTS LIST SERIALIZERS


# ADD PRODUCTS SERIALIZERS

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id", "product_code"]

# ADD PRODUCTS SERIALIZERS


# UPDATE PRODUCTS SERIALIZERS

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id", "product_code"]

# UPDATE PRODUCTS SERIALIZERS