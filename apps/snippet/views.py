import re

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from .forms import ArticleForm
from .models import *
from apps.comment.models import Comment
from ..comment.forms import CreateCommentForm
from ..favor.forms import FavorForm
from ..favor.models import Favor
from django.conf import settings


class ArticleListView(ListView):
    # model = Article
    paginate_by = 10
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
        # url_query_str = self.request.GET.urlencode()  # page=1&tag=flask
        # context['url_query'] = re.sub(r'page=\d*', '', url_query_str)  # &tag=flask

        # 获取带省略号的中间页码
        # context['elided_page_range'] = context['paginator'].get_elided_page_range(context['page_obj'].number)

        context['all_tags'] = Tag.objects.all()
        return context


def article_detail_view(request, pk):
    # 获取取单个 content_type
    content_type = ContentType.objects.get_for_model(Article)
    all_count = Comment.objects.filter(
                content_type=content_type,
                object_id=pk).all().count() // settings.COMMENT_PAGE_SIZE

    if request.htmx:
        page = int(request.GET.get('page'))
        start = (page - 1) * settings.COMMENT_PAGE_SIZE
        end = start + settings.COMMENT_PAGE_SIZE
        comment_list = Comment.objects.filter(content_type=content_type, object_id=pk)[start:end]
        page += 1

        return render(request, 'comment/htmx/comment_list.html', context={
            'comment_list': comment_list,
        })

    if request.method == 'GET':
        # 取单个 article
        article = get_object_or_404(Article, pk=pk)
        # 获取当前 article 的评论
        # comment_list = Comment.objects.filter(content_type=content_type, object_id=pk).all()
        comment_list = Comment.objects.filter(
            content_type=content_type,
            object_id=pk).all()[:settings.COMMENT_PAGE_SIZE]

        # 分页
        # paginator = Paginator(comment_list, 10)
        # page_number = request.GET.get('page', '1')
        # page_obj = paginator.get_page(page_number)
        # elided_page_range = paginator.get_elided_page_range(page_obj.number)

        # 收藏, 星星的显示状态
        if request.user.is_authenticated:
            is_favor = Favor.objects.filter(
                content_type=content_type,
                object_id=article.pk,
                author=request.user
            ).exists()
        else:
            is_favor = False

        # 传递默认值到模板的表单
        initial_data = {
            "object_id": article.id,
            'content_type': content_type,
            'author': request.user
        }
        # 评论表单设置默认值
        create_comment_form = CreateCommentForm(initial=initial_data)

        # 收藏表单设置默认值
        favor_form = FavorForm(initial=initial_data)

        return render(request, 'snippet/article_detail.html', context={
            "article": article,
            'create_comment_form': create_comment_form,
            "comment_list": comment_list,
            # 'page_obj': page_obj,
            # 'elided_page_range': elided_page_range,
            'is_favor': is_favor,
            'favor_form': favor_form,
            'all_count': all_count,
        })


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'snippet/article_create.html'

    def get_initial(self):
        return {'author': self.request.user}


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


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name_suffix = '_update_form'  # 自动找 article_update_form.html
    form_class = ArticleForm
