from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UsersListSerializer, UpdateUserSerializer, UpdateUsersPasswordSerializer, AdminListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from User.models import User
from .serializers import GetUserDetailSerializer
# Create your views here.


# USERS DETAIL VIEWS
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_user_detail_api_view(request: Request):
    try:
        if request.method == "POST":
            get_username = request.user
            print(request.user)
            get_user = User.objects.filter(username = get_username).first()
            serializer = GetUserDetailSerializer(get_user)
            return Response(serializer.data, status.HTTP_200_OK)
    except:
        return Response({"Detail" : "You Are Not Authenticated"}, status.HTTP_401_UNAUTHORIZED)


# USERS LIST VIEWS
class UsersListGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer


# UPDATE USERS VIEWS
@api_view(["PUT"])
def update_user_password(request: Request, user_code):
    if request.method == "PUT":
        user = User.objects.filter(user_code = user_code).first()
        serializer = UpdateUsersPasswordSerializer(data=request.data)
        user.set_password(serializer.data["password"])
        return Response({"detail" : "Password Was Changed Successfully"}, status.HTTP_202_ACCEPTED)

class UpdateUserGenericApiView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    lookup_field = "user_code"
    lookup_url_kwarg = "user_code"


# DELETE USERS
class DeleteUserGenericApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "user_code"
    lookup_url_kwarg = "user_code"


# ADMINS LIST VIEWS
class AdminsListGenericApiView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser = True)
    serializer_class = AdminListSerializer