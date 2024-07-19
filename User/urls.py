from django.urls import path
from .views import UsersListGenericApiView, UpdateUserGenericApiView, DeleteUserGenericApiView, update_user_password, AdminsListGenericApiView
urlpatterns = [
    path('users/', UsersListGenericApiView.as_view()),
    path('users/update/<user_code>/', UpdateUserGenericApiView.as_view()),
    path('users/update-password/<user_code>/', update_user_password),
    path('users/delete/<user_code>/', DeleteUserGenericApiView.as_view()),
    path('users/admins/', AdminsListGenericApiView.as_view())
]
