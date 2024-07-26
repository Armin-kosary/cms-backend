from django.shortcuts import render
from .models import Comment
from rest_framework import generics
from .serializers import CommentsListSerializer, UpdateCommentSerializer
# Create your views here.


# COMMENTS LIST VIEWS
class CommentsListGenericApiView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsListSerializer


# UPDATE COMMENTS VIEWS
class UpdateCommentGenerivApiView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = UpdateCommentSerializer
    lookup_field = "comment_code"
    lookup_url_kwarg = "comment_code"


# DELETE COMMENTS VIEWS
class DeleteCommentGenericApiView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = "comment_code"
    lookup_url_kwarg = "comment_code"