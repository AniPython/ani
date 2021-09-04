from django.db import models


class LearningResources(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    desc = models.TextField()
    order = models.PositiveSmallIntegerField('排序', default=100)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = '学习资源'
        verbose_name_plural = verbose_name

