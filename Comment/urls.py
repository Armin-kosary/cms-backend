from django.urls import path
from .views import CommentsListGenericApiView, UpdateCommentGenerivApiView, DeleteCommentGenericApiView

urlpatterns = [
    path('comments/', CommentsListGenericApiView.as_view()),
    path('comments/update/<comment_code>/', UpdateCommentGenerivApiView.as_view()),
    path('comments/delete/<comment_code>/', DeleteCommentGenericApiView.as_view())
]