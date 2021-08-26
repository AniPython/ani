
from django.http import HttpResponse
from django.urls import path

from .views import create_comment_view

app_name = 'comment'
urlpatterns = [
    path('create/', create_comment_view, name='create'),
]
