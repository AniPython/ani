from django import forms


class CreateCommentForm(forms.Form):
    content = forms.CharField()
    object_id = forms.CharField()
    content_type_id = forms.CharField()
