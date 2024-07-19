from django.urls import path
from .views import DiscountsListGenericApiView, UpdateDiscountGenericApiView, DeleteDiscountGenericApiView
urlpatterns = [
    path('discounts/', DiscountsListGenericApiView.as_view()),
    path('discounts/update/<discount_code>/', UpdateDiscountGenericApiView.as_view()),
    path('discounts/delete/<discount_code>/', DeleteDiscountGenericApiView.as_view())
]
