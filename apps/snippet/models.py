from django.db import models
from shortuuidfield import ShortUUIDField
from tinymce.models import HTMLField



class SnippetTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Snippet(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.CharField('标题', max_length=200)
    content = HTMLField('正文')
    tag = models.ManyToManyField('SnippetTag')
    author = models.ForeignKey('aniuser.AniUser', on_delete=models.SET_NULL, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '代码片段'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = HTMLField('正文')
    snippet = models.ForeignKey('Snippet', on_delete=models.CASCADE)
    author = models.ForeignKey('aniuser.AniUser', on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

snippet = Snippet.objects.all().first()

snippet.tag