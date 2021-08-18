from django.shortcuts import render
from django.http import HttpResponse


def pandas_index(request):
    return render(request, 'pandas/index.html')

