from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import *


class SnippetListView(ListView):
    model = Snippet
    paginate_by = 3

    template_name = 'snippet/snippet_index.html'
