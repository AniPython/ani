"""ani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.shortcuts import render, redirect
import allauth.account.urls


def index(request):
    return render(request, 'index.html', context={'index': True})


def video(request):
    return render(request, 'video.html')


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('myaccounts/', include('apps.aniuser.urls', namespace='ani')),
    # path('tinymce/', include('tinymce.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('crawler/', include('apps.crawler.urls', namespace='crawler')),
    path('user/', include('apps.aniuser.urls')),
    path('video/', video, name='video'),
    path('snippet/', include('apps.snippet.urls')),
    path('comment/', include('apps.comment.urls')),
    path('favor/', include('apps.favor.urls')),
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

# mdeditor
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# mdeditor 开始 ##########################################
MDEDITOR_CONFIGS = {
    'default': {
        'width': '100%',  # 自定义编辑框宽度
        'heigth': 500,  # 自定义编辑框高度
        'toolbar': ["undo", "redo", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "bold", "del", "italic", "quote", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "image", "code", "code-block", "table", "|",
                    "help",
                    "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
        'image_folder': 'editor',  # 图片保存文件夹名称
        'theme': 'default',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'sequence': True,  # 是否开启序列图功能
        'watch': True,  # 实时预览
        'lineWrapping': False,  # 自动换行
        'lineNumbers': True  # 行号
    },
    'comment': {
        'width': '100%',  # 自定义编辑框宽度
        'heigth': 200,  # 自定义编辑框高度
        'toolbar': ["h1", "h2", "h3", "h5", "h6", "|",
                    "bold", "del", "italic", "quote", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "image", "code", "code-block", "table", "|",
                    "help",
                    "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
        'image_folder': 'editor',  # 图片保存文件夹名称
        'theme': 'default',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'sequence': True,  # 是否开启序列图功能
        'watch': True,  # 实时预览
        'lineWrapping': False,  # 自动换行
        'lineNumbers': True  # 行号
    }
}
# mdeditor 结束 ##########################################
