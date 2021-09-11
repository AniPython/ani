from apps.aniuser.models import AniUser
from django import forms



class ProfileForm(forms.ModelForm):
    class Meta:
        model = AniUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']
