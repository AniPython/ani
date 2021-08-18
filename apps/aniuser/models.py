from django.contrib.auth.models import AbstractUser
from django.db import models


class AniUser(AbstractUser):
    phone = models.CharField('手机号码', max_length=11)

