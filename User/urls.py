from django.urls import path
from .views import UsersListGenericApiView, UpdateUserGenericApiView, DeleteUserGenericApiView, update_user_password, AdminsListGenericApiView, get_user_detail_api_view
urlpatterns = [
    # USERS LIST URLS
    path('users/', UsersListGenericApiView.as_view()),

    # USERS DETAIL URLS
    path('users/detail/', get_user_detail_api_view),

    # UPDATE USERS URLS
    path('users/update/<user_code>/', UpdateUserGenericApiView.as_view()),
    path('users/update-password/<user_code>/', update_user_password),
    
    # DELETE USERS URLS
    path('users/delete/<user_code>/', DeleteUserGenericApiView.as_view()),

    # ADMIN USERS LIST URLS
    path('users/admins/', AdminsListGenericApiView.as_view()),
]
