import re

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from mdeditor.fields import MDTextField
from shortuuidfield import ShortUUIDField

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveSmallIntegerField('排序', default=100)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    id = ShortUUIDField(primary_key=True, max_length=16)
    title = models.CharField('标题', max_length=200)
    content = RichTextUploadingField('正文', config_name='content-custom-toolbar')
    tag = models.ManyToManyField(Tag, verbose_name='标签',
                                 help_text='标签按住 win 的 Control 键或者 Mac 的 Command 键可多选')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='作者')
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

    # def save(self, *args, **kwargs):
    #     self.content = re.sub(r'\s*<p>(\s*&nbsp;\s*)*</p>\s*', '', self.content, flags=re.S)
    #     super().save(*args, **kwargs)
