from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from apps.aniuser.forms import RegisterFrom
from django.views.decorators.csrf import csrf_exempt


# def register(request):
#     if request.method == "POST":
#         form = RegisterFrom(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#         else:
#             return render(request, 'aniuser/register.html', context={'form': form})
#
#     form = RegisterFrom
#     return render(request,
#                   'aniuser/register.html',
#                   context={'form': form})
#
#
# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request=request,
#                                   data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')
#         else:
#             return redirect('aniuser:login')
#     else:
#         form = AuthenticationForm()
#         return render(request, "aniuser/login.html", context={"form": form})
#
#
# def logout_request(request):
#     logout(request)
#     return redirect('index')
from django.views.generic import DetailView, UpdateView, ListView

# @login_required(login_url='/accounts/login/')
# def profile(request):
#     return render(request, "aniuser/profile.html")



# @login_required(login_url='/accounts/login/')
# def profile_update(request):
#     return render(request, "aniuser/profile.html")
from .forms import ProfileForm
from .models import AniUser
from ..favor.models import Favor
from ..snippet.models import Article


# class ProfileView(LoginRequiredMixin, DetailView):
#     model = AniUser
#     template_name = 'aniuser/profile.html'


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
