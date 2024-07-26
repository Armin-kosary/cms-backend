from django.shortcuts import render
from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrdersListSerializer, OrderDetailSerializer, OrderItemSerializer, UpdateOrdersSerializer
# Create your views here.


# ORDERS LIST
class OrdersListGenericApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersListSerializer


# ORDERS DETAIL VIEWS
class OrderDetailGenericApiView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = "order_code"
    lookup_url_kwarg = "order_code"

class OrderItemsGenericApiView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = "order__order_code"
    lookup_url_kwarg = "order_code"


# UPDATE ORDERS VIEW
class UpdateOrderGenericApiView(generics.UpdateAPIView):
    serializer_class = UpdateOrdersSerializer
    lookup_field = "order_code"
    lookup_url_kwarg = "order_code"
    queryset = Order.objects.all()
        

# DELETE ORDERS VIEW
class DeleteOrderGenericApiView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    lookup_field = "order_code"
    lookup_url_kwarg = "order_code"