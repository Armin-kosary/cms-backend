from django.urls import path
from .views import OrdersListGenericApiView, OrderDetailGenericApiView, OrderItemsGenericApiView, DeleteOrderGenericApiView

urlpatterns = [
    # ORDERS LIST
    path('orders/', OrdersListGenericApiView.as_view()),

    # ORDERS DETAIL URLS
    path('orders/detail/<order_code>/', OrderDetailGenericApiView.as_view()),
    path('orders/detail/items/<order_code>/', OrderItemsGenericApiView.as_view()),
    
    # DELETE ORDERS URLS
    path('orders/delete/<order_code>/', DeleteOrderGenericApiView.as_view())
]
