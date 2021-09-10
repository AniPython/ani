from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from shortuuidfield import ShortUUIDField
from django.shortcuts import reverse

from apps.favor.models import Favor
from apps.snippet.models import Article


class AniUser(AbstractUser):
    id = ShortUUIDField(primary_key=True)
    phone = models.CharField('手机号码', max_length=11, blank=True, null=True)

    def get_favor_snippet_articles(self):
        content_type = ContentType.objects.get_for_model(Article)
        favors = Favor.objects.filter(content_type=content_type, author=self)
        articles = Article.objects.filter(id__in=[i.object_id for i in favors])
        return articles

    def get_absolute_url(self):
        return reverse('aniuser:profile')
