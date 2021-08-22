
from django.http import HttpResponse
from django.urls import path

from .views import *

app_name = 'snippet'
urlpatterns = [
    path('', SnippetListView.as_view(), name='index'),
    path('<str:pk>', SnippetDetailView.as_view(), name='detail'),
    path('post_comment/', post_comment, name='post_comment'),
]
