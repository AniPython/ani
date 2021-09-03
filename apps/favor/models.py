from django.contrib.contenttypes.models import ContentType
from django.db import models


class Favor(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField('收藏对象ID', max_length=22, null=True)
    author = models.ForeignKey('aniuser.AniUser', on_delete=models.CASCADE, verbose_name='作者')

    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name


