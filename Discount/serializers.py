from rest_framework import serializers
from .models import Discount

class DiscounstListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ["id"]


class UpdateDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["is_active"]