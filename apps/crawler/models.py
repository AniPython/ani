from django.db import models


class LearningResources(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    desc = models.TextField()
