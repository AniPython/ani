from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.aniuser.forms import RegisterFrom
from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'aniuser/register.html', context={'form': form})

    form = RegisterFrom
    return render(request,
                  'aniuser/register.html',
                  context={'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,
                                  data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('aniuser:login')

    form = AuthenticationForm()
    return render(request, "aniuser/login.html", context={"form": form})


def logout_request(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/user/login/')
def profile(request):
    return render(request, "aniuser/profile.html")
