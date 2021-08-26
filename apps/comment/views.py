from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateCommentForm
from .models import Comment


@login_required
def create_comment_view(request):
    if request.method == "POST":
        form = CreateCommentForm(request.POST or None)
        if form.is_valid():
            print('验证成功')

            content = form.cleaned_data.get('content')
            object_id = form.cleaned_data.get('object_id')
            content_type_id = form.cleaned_data.get('content_type_id')

            comment = Comment.objects.create(
                content=content,
                object_id=object_id,
                content_type_id=content_type_id,
                author=request.user
            )

            return redirect(f'/snippet/article/{comment.object_id}')
        else:
            return HttpResponse(str(form.errors) + '字段出错了')
