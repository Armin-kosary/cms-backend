from django.shortcuts import render
from rest_framework import generics
from .models import Discount
from .serializers import DiscounstListSerializer, AddDiscountSerializer, UpdateDiscountSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from User.models import User
# Create your views here.

# DISCOUNTS LIST VIEWS
class DiscountsListGenericApiView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscounstListSerializer


# ADD DISCOUNTS VIEWS
@api_view(["POST"])
def add_discount_api_view(request: Request):
    serialializer = AddDiscountSerializer(data=request.data)
    if serialializer.is_valid():
        user = User.objects.filter(username = request.user).first()

        new_discount = Discount(title = serialializer.data["title"],
                                percent = serialializer.data["percent"],
                                key = serialializer.data["key"],
                                author = user,
                                is_active = serialializer.data["is_active"])
        new_discount.save()
        return Response(serialializer.data, status.HTTP_201_CREATED)


# UPDATE DISCOUNTS VIEWS
class UpdateDiscountGenericApiView(generics.UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = UpdateDiscountSerializer
    lookup_field = "discount_code"
    lookup_url_kwarg = "discount_code"


# DELETE DISCOUNTS VIEWS
class DeleteDiscountGenericApiView(generics.DestroyAPIView):
    queryset = Discount.objects.all()
    lookup_field = "discount_code"
    lookup_url_kwarg = "discount_code"