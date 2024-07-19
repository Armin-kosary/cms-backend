from rest_framework import serializers
from .models import Product


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id"]

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id", "product_code"]

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id", "product_code"]