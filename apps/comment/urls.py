
from django.http import HttpResponse
from django.urls import path

from .views import create_comment_view, CommentUpdateView, CommentDeleteView

app_name = 'comment'
urlpatterns = [
    path('create/', create_comment_view, name='create'),
    path('<str:pk>/change/', CommentUpdateView.as_view(), name='change'),
    path('<str:pk>/delete/', CommentDeleteView.as_view(), name='delete'),
]
