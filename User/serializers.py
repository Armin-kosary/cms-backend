from rest_framework import serializers
from .models import User

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id", "is_staff", "is_active", "date_joined", "password", "last_login", "groups", "user_permissions"]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "phone", "city", "email", "address", "score", "buy", "user_code"]


class UpdateUsersPasswordSerializer(serializers.Serializer):
    password = serializers.CharField


class AdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]