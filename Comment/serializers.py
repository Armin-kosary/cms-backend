from rest_framework import serializers
from .models import Comment
from User.models import User

class CommentsOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class CommentsListSerializer(serializers.ModelSerializer):
    user = CommentsOwnerSerializer()
    class Meta:
        model = Comment
        exclude = ["id"]

class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["id", "user", "comment_code"]