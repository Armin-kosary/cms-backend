from rest_framework import serializers
from .models import Comment
from User.models import User
from Product.models import Product

# COMMENTS LIST SERIALIZERS

class CommentsOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class CommentsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "product_code"]

class CommentsListSerializer(serializers.ModelSerializer):
    user = CommentsOwnerSerializer()
    product = CommentsProductSerializer()
    class Meta:
        model = Comment
        exclude = ["id"]

# COMMENTS LIST SERIALIZERS


# UPDATE COMMENTS SERIALIZERS

class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["id", "user", "comment_code", "content", "product"]

# UPDATE COMMENTS SERIALIZERS