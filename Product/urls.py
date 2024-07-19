from django.urls import path
from .views import ProductListGenericApiView, AddProductGenericApiView, UpdateProductGenericApiView, DeleteProductGenericApiView

urlpatterns = [
    path('products/', ProductListGenericApiView.as_view()),
    path('products/add/', AddProductGenericApiView.as_view()),
    path('products/update/<product_code>/', UpdateProductGenericApiView.as_view()),
    path('products/delete/<product_code>/', DeleteProductGenericApiView.as_view())
]
