from django import forms
from .models import Article
import re


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tag', 'author']
        widgets = {'author': forms.HiddenInput}

    def clean_content(self):
        content = self.cleaned_data['content']
        content = re.sub(r'\s*<p>(\s*&nbsp;\s*)*</p>\s*', '', content, flags=re.S)
        return content
