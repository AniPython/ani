from django.contrib import admin

from .models import Tag, Article


admin.site.register(Tag)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    readonly_fields = ['create_time', 'update_time']


