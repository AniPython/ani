from ckeditor.fields import RichTextField
from django.contrib.contenttypes.models import ContentType
from django.db import models
from shortuuidfield import ShortUUIDField


class Comment(models.Model):
    id = ShortUUIDField(primary_key=True, max_length=16)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField('评论对象ID', max_length=22, null=True)
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

    def get_absolute_url(self):
        return self.get_father().get_absolute_url()

    def get_father(self):
        father_model_class = self.content_type.model_class()
        father = father_model_class.objects.get(pk=self.object_id)
        return father

