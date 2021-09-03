
from django.http import HttpResponse
from django.urls import path

from .views import favor_view

app_name = 'favor'
urlpatterns = [
    path('toggle/', favor_view, name='toggle_favor'),
]
