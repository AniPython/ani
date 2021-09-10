
from django.http import HttpResponse
from django.urls import path

from .views import *

app_name = 'snippet'
urlpatterns = [
    path('article/', ArticleListView.as_view(), name='list'),
    path('article/create/', ArticleCreateView.as_view(), name='create'),
    path('article/<str:pk>/', article_detail_view, name='detail'),
    path('article/<str:pk>/change/', ArticleUpdateView.as_view(), name='change'),
    path('article/<str:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
]
