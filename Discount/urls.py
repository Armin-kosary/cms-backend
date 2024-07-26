from django.urls import path
from .views import DiscountsListGenericApiView, add_discount_api_view, UpdateDiscountGenericApiView, DeleteDiscountGenericApiView
urlpatterns = [
    path('discounts/', DiscountsListGenericApiView.as_view()),
    path('discounts/add/', add_discount_api_view),
    path('discounts/update/<discount_code>/', UpdateDiscountGenericApiView.as_view()),
    path('discounts/delete/<discount_code>/', DeleteDiscountGenericApiView.as_view()),
]
