
from django.http import HttpResponse
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

app_name = 'aniuser'
# urlpatterns = [
    # path('register/', register, name='register'),
    # path('login/', login_request, name='login'),
    # path('login/', LoginView.as_view(template_name='aniuser/login.html'), name='login'),
    # path('logout/', logout_request, name='logout'),
    # path('profile/', profile, name='profile'),
    # path('profile/articles/', ProfileArticlesView.as_view(), name='profile_articles'),
    # path('<str:pk>/profile/', ProfileView.as_view(), name='profile'),
    # path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
# ]

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/update/<str:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/articles/', ProfileArticlesView.as_view(), name='profile_articles'),
    path('profile/favor_articles/', ProfileFavorArticlesView.as_view(), name='profile_favor_articles'),
]
