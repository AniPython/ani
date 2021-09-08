import re

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateCommentForm
from .models import Comment
from ..snippet.models import Article


@login_required
def create_comment_view(request):
    if request.method == "POST":
        form = CreateCommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save()
            return redirect(f'/snippet/article/{comment.object_id}')
        else:
            return HttpResponse(str(form.errors))



