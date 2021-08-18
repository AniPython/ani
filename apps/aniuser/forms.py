from django.contrib.auth.forms import UserCreationForm, UsernameField

from apps.aniuser.models import AniUser


class RegisterFrom(UserCreationForm):
    class Meta:
        model = AniUser
        fields = ("username",)
        field_classes = {'username': UsernameField}
