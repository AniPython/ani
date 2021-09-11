from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import UpdateView, ListView
from .forms import ProfileForm
from .models import AniUser
from ..snippet.models import Article


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, "aniuser/profile.html")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = AniUser
    template_name = 'aniuser/profile_update.html'
    form_class = ProfileForm


class ProfileArticlesView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'aniuser/profile_my_articles.html'


class ProfileFavorArticlesView(LoginRequiredMixin, ListView):
    template_name = 'aniuser/profile_my_articles.html'

    def get_queryset(self):
        return self.request.user.get_favor_snippet_articles()
