from django.urls import path
from .views import ProductListGenericApiView, AddProductGenericApiView, UpdateProductGenericApiView, DeleteProductGenericApiView

urlpatterns = [
    # PRODUCTS LISTS URLS
    path('products/', ProductListGenericApiView.as_view()),

    # ADD PRODUCTS URLS
    path('products/add/', AddProductGenericApiView.as_view()),

    # UPDATE PRODUCTS URLS
    path('products/update/<product_code>/', UpdateProductGenericApiView.as_view()),

    # DELETE PRODUCTS URLS
    path('products/delete/<product_code>/', DeleteProductGenericApiView.as_view())
]
