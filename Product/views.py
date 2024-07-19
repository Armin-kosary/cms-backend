from django.shortcuts import render
from .models import Product
from .serializers import ProductsListSerializer, AddProductSerializer, UpdateProductSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework import generics
# Create your views here.

class ProductListGenericApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

class AddProductGenericApiView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = AddProductSerializer

class UpdateProductGenericApiView(generics.UpdateAPIView):
    parser_classes = [MultiPartParser]
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
    lookup_field = "product_code"
    lookup_url_kwarg = "product_code"

class DeleteProductGenericApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = "product_code"
    lookup_url_kwarg = "product_code"