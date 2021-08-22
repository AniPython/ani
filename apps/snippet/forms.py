from django.forms import ModelForm
from django import forms
from .models import Comment


class PostCommentForm(forms.Form):
    content = forms.CharField()
    snippet_id = forms.CharField()
