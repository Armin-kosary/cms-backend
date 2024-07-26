from rest_framework import serializers
from .models import Discount
from User.models import User


# DISCOUNTS LIST SERIALIZERS

class DiscountsListsOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class DiscounstListSerializer(serializers.ModelSerializer):
    author = DiscountsListsOwnersSerializer()
    class Meta:
        model = Discount
        exclude = ["id"]

# DISCOUNTS LIST SERIALIZERS


# ADD DISCOUNTS SERIALIZERS

class AddDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ["id", "author"]

# ADD DISCOUNTS SERIALIZERS


# UPDATE DISCOUNTS SERIALIZERS

class UpdateDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["is_active"]

# UPDATE DISCOUNTS SERIALIZERS