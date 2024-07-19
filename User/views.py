from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UsersListSerializer, UpdateUserSerializer, UpdateUsersPasswordSerializer, AdminListSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UsersListGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer

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

class DeleteUserGenericApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "username"
    lookup_url_kwarg = "username"


class AdminsListGenericApiView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser = True)
    serializer_class = AdminListSerializer