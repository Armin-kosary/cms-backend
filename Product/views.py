from django.shortcuts import render
from .models import Product
from .serializers import ProductsListSerializer, AddProductSerializer, UpdateProductSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework import generics
# Create your views here.

# PRODUCTS LIST VIEWS
class ProductListGenericApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


# ADD PRODUCTS VIEWS
class AddProductGenericApiView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = AddProductSerializer


# UPDATE PRODUCTS VIEWS
class UpdateProductGenericApiView(generics.UpdateAPIView):
    parser_classes = [MultiPartParser]
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
    lookup_field = "product_code"
    lookup_url_kwarg = "product_code"


# DELETE PRODUCTS VIEWS
class DeleteProductGenericApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = "product_code"
    lookup_url_kwarg = "product_code"