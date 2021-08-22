from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostCommentForm
from .models import *


class SnippetListView(ListView):
    model = Snippet
    paginate_by = 5

    template_name = 'snippet/snippet_index.html'

    def get_queryset(self):
        tag = self.request.GET.get('tag', '')
        if tag:
            return Snippet.objects.filter(tag__name__contains=tag)
        else:
            return Snippet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = self.request.GET.get('tag', '')
        context['url_query'] = f'&tag={tag}'
        context['all_tags'] = SnippetTag.objects.all()

        # 获取带省略号的中间页码
        context['elided_page_range'] = context['paginator'].get_elided_page_range(context['page_obj'].number)

        return context


class SnippetDetailView(ListView):
    """
    既是
    SnippetDetailView
    又是
    CommentListView
    """
    # model = Comment
    paginate_by = 5
    template_name = 'snippet/snippet_detail.html'

    @property
    def snippet_id(self):
        return self.request.path.replace('/snippet/', '')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snippet'] = Snippet.objects.get(pk=self.snippet_id)

        # 获取带省略号的中间页码
        context['elided_page_range'] = context['paginator'].get_elided_page_range(context['page_obj'].number)

        return context

    def get_queryset(self):
        comment_list = Comment.objects.filter(snippet__id=self.snippet_id)
        return comment_list


@login_required
def post_comment(request):
    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            snippet_id = form.cleaned_data.get('snippet_id')
            Comment.objects.create(
                content=content,
                snippet_id=snippet_id,
                author=request.user
            )
            return redirect(f'/snippet/{snippet_id}')
        else:
            return HttpResponse('评论出错了')


class SnippetCreateView(CreateView):
    model = Snippet
    fields = ['title', 'content', 'tag']
    template_name = 'snippet/snippet_create.html'


    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            title = request.POST.get('title')
            content = request.POST.get('content')
            author_id = request.POST.get('author_id')
            tag_id_list = request.POST.getlist('tag')

            # 创建文章
            snippet = Snippet.objects.create(title=title,
                                             content=content,
                                             author_id=author_id,
                                             )

            # 给文章添加标签
            for tag_id in tag_id_list:
                tag = SnippetTag.objects.get(id=int(tag_id))
                tag.snippet_set.add(snippet)

            return redirect('snippet:index')
        else:
            return render(request, 'snippet/snippet_create.html', context={'form': form})
