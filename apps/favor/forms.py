from django import forms


class FavorForm(forms.Form):
    object_id = forms.CharField()
    content_type_id = forms.CharField()
    is_favor = forms.CharField()
