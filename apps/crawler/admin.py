from django.contrib import admin

from .models import LearningResources


@admin.register(LearningResources)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'desc']
