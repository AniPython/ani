from django import forms
from .models import Favor


class FavorForm(forms.ModelForm):

    # object_id = forms.CharField()
    # content_type_id = forms.CharField()
    # is_favor = forms.CharField()

    class Meta:
        model = Favor
        fields = ['author', 'object_id', 'content_type']
        widgets = {
            'author': forms.HiddenInput,
            'object_id': forms.HiddenInput,
            'content_type': forms.HiddenInput,
        }


    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.CharField('收藏对象ID', max_length=22, null=True)
    # author = models.ForeignKey('aniuser.AniUser', on_delete=models.CASCADE, verbose_name='作者')