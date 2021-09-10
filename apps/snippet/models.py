import re

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from shortuuidfield import ShortUUIDField

# User = get_user_model()
from apps.comment.models import Comment
from apps.favor.models import Favor


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveSmallIntegerField('排序', default=100)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @property
    def get_article_amount(self):
        return Article.objects.filter(tag__name__contains=self.name).count()

    def get_all(self):
        return Article.objects.all().count()


class Article(models.Model):
    id = ShortUUIDField(primary_key=True, max_length=16)
    title = models.CharField('标题', max_length=200)
    content = RichTextUploadingField('正文', config_name='content-custom-toolbar')
    tag = models.ManyToManyField(Tag, verbose_name='标签',
                                 help_text='标签按住 win 的 Control 键或者 Mac 的 Command 键可多选')
    author = models.ForeignKey('aniuser.AniUser', on_delete=models.SET_NULL, null=True, verbose_name='作者')
    is_active = models.BooleanField('是否显示文章', default=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def get_absolute_url(self):
        return f'/snippet/article/{self.id}/'

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    @property
    def get_favor_amount(self):
        content_type = ContentType.objects.get_for_model(Article)
        return Favor.objects.filter(content_type=content_type, object_id=self.id).count()

    @property
    def get_comment_amount(self):
        content_type = ContentType.objects.get_for_model(Article)
        return Comment.objects.filter(content_type=content_type, object_id=self.id).count()

