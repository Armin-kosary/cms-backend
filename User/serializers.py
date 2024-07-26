from rest_framework import serializers
from .models import User

# USERS DETAIL SERIALIZERS

class GetUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]

# USERS DETAIL SERIALIZERS


# USERS LIST SERIALIZERS

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id", "is_staff", "is_active", "date_joined", "password", "last_login", "groups", "user_permissions"]

# USERS LIST SERIALIZERS


# UPDATE USERS SERIALIZERS

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "phone", "city", "email", "address", "score", "buy", "user_code"]

class UpdateUsersPasswordSerializer(serializers.Serializer):
    password = serializers.CharField

# UPDATE USERS SERIALIZERS


# ADMINS LIST SERIALIZERS

class AdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

# ADMINS LIST SERIALIZERS