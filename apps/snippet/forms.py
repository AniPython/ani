from django.forms import ModelForm
from django import forms


class PostCommentForm(forms.Form):
    content = forms.CharField()
    snippet_id = forms.CharField()
