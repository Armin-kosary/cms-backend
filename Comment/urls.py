from django.urls import path
from .views import CommentsListGenericApiView, UpdateCommentGenerivApiView, DeleteCommentGenericApiView

urlpatterns = [
    # COMMENTS LIST URLS
    path('comments/', CommentsListGenericApiView.as_view()),

    # UPDATE COMMENTS URLS
    path('comments/update/<comment_code>/', UpdateCommentGenerivApiView.as_view()),
    
    # DELETE COMMENTS URLS
    path('comments/delete/<comment_code>/', DeleteCommentGenericApiView.as_view())
]