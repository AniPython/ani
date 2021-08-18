from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'crawler'
urlpatterns = [
    path('', crawler_index, name='index'),
    path('1/', crawler1, name='crawler1'),
    path('2/', crawler2, name='crawler2'),
    path('3/', crawler3, name='crawler3'),
    path('4/', Crawler4ListView.as_view(), name='crawler4_list'),
    path('4/<int:pk>', Crawler4DetailView.as_view(), name='crawler4_detail'),
    path('5/', crawler5, name='crawler5'),
    path('6/', crawler6, name='crawler6'),
    path('6/download_file', crawler6_download_file, name='crawler6_download_file'),
    path('7/', crawler7, name='crawler7'),
    path('8/', crawler8, name='crawler8'),
    path('8/api', crawler8_api, name='crawler8_api'),
]

# 不用经过 view 视图函数的 html
static_html = [
    path('4/crawler4',
         TemplateView.as_view(template_name='crawler/py_html/crawler4.py.html'),
         name='crawler4_py'),
    path('4/scrapy_crawler4',
         TemplateView.as_view(template_name='crawler/py_html/Ani.ani.spiders.crawler4.py.html'),
         name='scrapy_crawler4_py'),
    # path('5/',
    #      TemplateView.as_view(template_name='crawler/crawler5.html'),
    #      name='crawler5'),
    # path('5/scrawler5_py/',
    #      TemplateView.as_view(template_name='crawler/py_html/crawler5.py.html'),
    #      name='crawler5_py'),

]

urlpatterns += static_html
