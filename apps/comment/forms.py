import re
from django import forms
from .models import Comment


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', 'object_id', 'content_type', 'author']
        widgets = {
            'object_id': forms.HiddenInput,
            'content_type': forms.HiddenInput,
            'author': forms.HiddenInput,
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        content = re.sub(r'\s*<p>(\s*&nbsp;\s*)*</p>\s*', '', content, flags=re.S)
        return content
