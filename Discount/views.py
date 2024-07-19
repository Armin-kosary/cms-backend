from django.shortcuts import render
from rest_framework import generics
from .models import Discount
from .serializers import DiscounstListSerializer, UpdateDiscountSerializer
# Create your views here.

class DiscountsListGenericApiView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscounstListSerializer

class UpdateDiscountGenericApiView(generics.UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = UpdateDiscountSerializer
    lookup_field = "discount_code"
    lookup_url_kwarg = "discount_code"

class DeleteDiscountGenericApiView(generics.DestroyAPIView):
    queryset = Discount.objects.all()
    lookup_field = "discount_code"
    lookup_url_kwarg = "discount_code"