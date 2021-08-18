
from django.urls import path
from .views import pandas_index

app_name = 'pandas'
urlpatterns = [
    path('', pandas_index, name='index'),
]
