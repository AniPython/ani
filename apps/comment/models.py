from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField('评论对象ID', max_length=32, null=True)
    content = models.TextField('评论内容', max_length=1000)
    author = models.ForeignKey('aniuser.AniUser', on_delete=models.CASCADE, verbose_name='作者')
    is_active = models.BooleanField('是否显示', default=True)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:8]
