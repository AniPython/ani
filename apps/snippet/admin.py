from django.contrib import admin

from .models import SnippetTag, Snippet, Comment
# from django_comments.models import Comment


class SnippetCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(SnippetTag)
admin.site.register(Snippet)
admin.site.register(Comment)

