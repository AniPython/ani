from django.contrib.auth import get_user_model
from django.db import models
from shortuuidfield import ShortUUIDField
from tinymce.models import HTMLField

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.CharField('标题', max_length=200)
    content = HTMLField('正文')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
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
