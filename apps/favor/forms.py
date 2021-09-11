from django import forms
from .models import Favor


class FavorForm(forms.ModelForm):

    class Meta:
        model = Favor
        fields = ['author', 'object_id', 'content_type']
        widgets = {
            'author': forms.HiddenInput,
            'object_id': forms.HiddenInput,
            'content_type': forms.HiddenInput,
        }
