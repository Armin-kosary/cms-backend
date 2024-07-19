from django.urls import path
from .views import OrdersListGenericApiView, OrderDetailGenericApiView, OrderItemsGenericApiView

urlpatterns = [
    # ORDERS LIST
    path('orders/', OrdersListGenericApiView.as_view()),
    # ORDER DETAIL PAGE
    path('orders/detail/<order_code>/', OrderDetailGenericApiView.as_view()),
    path('orders/detail/items/<order_code>/', OrderItemsGenericApiView.as_view()),

    # path('orders/update/<order_code>/', ),
    # path('orders/delete/<order_code>/', ),
    # path('orders/delete-items/<order_code>/', ),
]
