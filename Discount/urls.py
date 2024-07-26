from django.urls import path
from .views import DiscountsListGenericApiView, add_discount_api_view, UpdateDiscountGenericApiView, DeleteDiscountGenericApiView
urlpatterns = [
    # DISCOUNTS LIST URLS
    path('discounts/', DiscountsListGenericApiView.as_view()),

    # ADD DISCOUNTS URLS
    path('discounts/add/', add_discount_api_view),

    # UPDATE DISCOUNTS URLS
    path('discounts/update/<discount_code>/', UpdateDiscountGenericApiView.as_view()),

    # DELETE DISCOUNTS URLS
    path('discounts/delete/<discount_code>/', DeleteDiscountGenericApiView.as_view()),
]
