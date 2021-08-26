import re

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from .models import *
from apps.comment.models import Comment


class ArticleListView(ListView):
    # model = Article
    paginate_by = 5

    template_name = 'snippet/article_list.html'

    def get_queryset(self):
        tag = self.request.GET.get('tag', '')
        if tag:
            return Article.objects.filter(tag__name__contains=tag).select_related('author').prefetch_related('tag')
        else:
            return Article.objects.all().select_related('author').prefetch_related('tag')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 翻页保留其它的 query string
        url_query_str = self.request.GET.urlencode()  # page=1&tag=flask
        context['url_query'] = re.sub(r'page=\d*', '', url_query_str)  # &tag=flask

        context['all_tags'] = Tag.objects.all()

        # 获取带省略号的中间页码
        context['elided_page_range'] = context['paginator'].get_elided_page_range(context['page_obj'].number)

        return context


def article_detail_view(request, pk):
    if request.method == 'GET':
        # 取单个 article
        article = get_object_or_404(Article, pk=pk)

        # 取这个 article 下面的评论
        content_type = ContentType.objects.get_for_model(Article)
        comment_list = Comment.objects.filter(content_type=content_type, object_id=pk).all()
        paginator = Paginator(comment_list, 3)
        page_number = request.GET.get('page', '1')
        # 分页导航需要的 page_obj 和 elided_page_range
        page_obj = paginator.get_page(page_number)
        print(page_obj)
        print(page_obj.number)
        elided_page_range = paginator.get_elided_page_range(page_obj.number)

        return render(request, 'snippet/article_detail.html', context={
            "article": article,
            "comment_list": comment_list,
            'page_obj': page_obj,
            'elided_page_range': elided_page_range,
            'content_type_id': content_type.id
        })


class ArticleDetailViewBackup(ListView):
    """
    既是
    SnippetDetailView
    又是
    CommentListView
    """
    # model = Comment
    paginate_by = 5
    template_name = 'snippet/article_detail.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.article_id = ''

    def get(self, request, *args, **kwargs):
        self.article_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=self.article_id)

        # 获取带省略号的中间页码
        context['elided_page_range'] = context['paginator'].get_elided_page_range(context['page_obj'].number)

        return context

    def get_queryset(self):
        comment_list = Comment.objects.filter(article__id=self.article_id)
        return comment_list


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'tag']
    template_name = 'snippet/article_create.html'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # # 创建文章
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # snippet = Snippet.objects.create(title=title,
            #                                  content=content,
            #                                  author=request.user)
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            # 给文章添加标签
            form.save_m2m()
            # tag_id_list = request.POST.getlist('tag')
            # for tag_id in tag_id_list:
            #     tag = SnippetTag.objects.get(id=int(tag_id))
            #     tag.snippet_set.add(snippet)

            return redirect(article.get_absolute_url())
        else:
            return render(request, 'snippet/article_create.html', context={'form': form})


def snippet_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.all()
    if query is not None:
        lookups = Q(title_icontains=query) | Q(content__icontains=query)
        qs = Article.objects.filter(lookups)
    context = {
        "object_list": qs
    }
    return render(request, "snippet/article_search.html", context=context)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'tag']
    template_name_suffix = '_update_form'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author != request.user:
            return HttpResponse('这不是你的文章, 不能编辑')
        return super().get(request, *args, **kwargs)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author != request.user:
            return HttpResponse('这不是你的文章, 不能编辑')
        return super().post(request, *args, **kwargs)
