from django.contrib.auth.models import AbstractUser
from django.db import models
from shortuuidfield import ShortUUIDField


class AniUser(AbstractUser):
    id = ShortUUIDField(primary_key=True, max_length=16)
    phone = models.CharField('手机号码', max_length=11)

