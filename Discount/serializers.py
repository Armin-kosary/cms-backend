from rest_framework import serializers
from .models import Discount
from User.models import User


class DiscountsListsOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class DiscounstListSerializer(serializers.ModelSerializer):
    author = DiscountsListsOwnersSerializer()
    class Meta:
        model = Discount
        exclude = ["id"]



class AddDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ["id", "author"]



class UpdateDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["is_active"]