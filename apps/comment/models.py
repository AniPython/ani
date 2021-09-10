import re

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.shortcuts import get_object_or_404
from shortuuidfield import ShortUUIDField

# from apps.snippet.models import Article


class Comment(models.Model):
    id = ShortUUIDField(primary_key=True, max_length=16)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField('评论对象ID', max_length=22, null=True)
    # content = models.TextField('评论内容', max_length=1000)
    content = RichTextField('评论', config_name='comment-custom-toolbar', null=False, blank=False)
    author = models.ForeignKey('aniuser.AniUser', on_delete=models.CASCADE, verbose_name='作者')
    is_active = models.BooleanField('是否显示', default=True)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:8]

    # def save(self, *args, **kwargs):
    #     self.content = re.sub(r'\s*<p>(\s*&nbsp;\s*)*</p>\s*', '', self.content, flags=re.S)
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        # father_model_class = self.content_type.model_class()
        # father = get_object_or_404(father_model_class, pk=self.object_id)
        return self.get_father().get_absolute_url()

    def get_father(self):
        father_model_class = self.content_type.model_class()
        father = father_model_class.objects.get(pk=self.object_id)
        return father

