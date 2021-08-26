from django import forms

from .models import Comment


class CreateCommentForm(forms.Form):
    # class Meta:
    #     model = Comment
    #     fields = ['content', 'object_id']
    content = forms.CharField()
    object_id = forms.CharField()
    content_type_id = forms.CharField()
