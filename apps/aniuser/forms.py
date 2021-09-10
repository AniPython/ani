from django.contrib.auth.forms import UserCreationForm, UsernameField

from apps.aniuser.models import AniUser
from django import forms


# class RegisterFrom(UserCreationForm):
#     class Meta:
#         model = AniUser
#         fields = ("username",)
#         field_classes = {'username': UsernameField}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = AniUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']
