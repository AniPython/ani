"""
Django settings for ani project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import socket

# is_production = False
# if socket.gethostname() == 'iZwz9945xduhq7zwqzvmmnZ':
#     is_production = True
# else:
#     is_production = False

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == '1'
# DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "anipython.com", "www.anipython.com", "39.108.112.236", "192.168.1.100"]

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # 手动加
    'debug_toolbar',

    # 'ckeditor',
    # 'ckeditor_uploader',

    'mdeditor',

    'apps.aniuser',
    'apps.crawler',
    'apps.comment',
    'apps.snippet',
    'apps.favor',

    'bootstrap4',
    'django_htmx',
    'star_ratings',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.baidu',

]

X_FRAME_OPTIONS = 'SAMEORIGIN'

SITE_ID = 3

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = 'ani.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ani_utils.context_processors.get_is_active',
            ],
        },
    },
]

WSGI_APPLICATION = 'ani.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ani',
        'USER': 'root',
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# collectstatic 将收集静态文件进行部署的目录的绝对路径
STATIC_ROOT = BASE_DIR / 'static_dist'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 自定义用户
AUTH_USER_MODEL = 'aniuser.AniUser'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'uploads'
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/snippet/article/'

INTERNAL_IPS = [
    '127.0.0.1',
    '39.108.112.236',
]

# django-allauth 开始 ######################################################
AUTHENTICATION_BACKENDS = (
    # Django 自带的用用户名登录，独立于allauth
    'django.contrib.auth.backends.ModelBackend',
    # 配置 allauth 独有的认证方法，如 email 登录
    'allauth.account.auth_backends.AuthenticationBackend',
)

# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'的作用是当用户登录时，
# 既可以使用用户名也可以使用email， 其他可选的值是 username 、 email
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

# 设置用户注册的时候必须填写邮箱地址
ACCOUNT_EMAIL_REQUIRED = True

# 登出直接退出，不用确认
ACCOUNT_LOGOUT_ON_GET = True

# 第三方登录设置
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': '2e2a783e6bc444c720ab',
            'secret': os.environ.get('GITHUB_SECRET'),
            'key': ''
        }
    },
}

# 邮箱检验
# mandatory: 发送电子邮件, 通过检验才能登录
# optional(默认): 发送电子邮件, 不通过检验也可以登录
# none: 不发送电子邮件, 不通过检验也可以登录
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# 第三方登录不需要检验邮箱
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

# 在终端打印出邮箱发送的内容
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# allauth 邮箱设定 (qq邮箱)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
# EMAIL_PORT = 25  # http
EMAIL_PORT = 465  # https
EMAIL_HOST_USER = '37013823@qq.com'
EMAIL_FROM = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True  # http
EMAIL_USE_SSL = True  # https
# django-allauth 结束 ######################################################


# ckeditor 开始 ######################################################
# CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
# CKEDITOR_UPLOAD_PATH = 'ckeditor/'
# CUSTOM_TOOLBAR = [
#     {
#         "name": "document",
#         "items": [
#             "Styles",
#             "Format",
#             'Font',
#             'FontSize',
#             "Bold",
#             "Italic",
#             "Underline",
#             "Strike",
#             "-",
#             "TextColor",
#             "BGColor",
#             "-",
#             "JustifyLeft",
#             "JustifyCenter",
#             "JustifyRight",
#             "JustifyBlock",
#         ],
#     },
#     {
#         "name": "widgets",
#         "items": [
#             "codesnippet",
#             "Undo",
#             "Redo",
#             "-",
#             "NumberedList",
#             "BulletedList",
#             "-",
#             "Outdent",
#             "Indent",
#             "-",
#             "Link",
#             "Unlink",
#             "-",
#             "Image",
#             "CodeSnippet",
#             "Table",
#             "HorizontalRule",
#             "Smiley",
#             "SpecialChar",
#             "-",
#             "Blockquote",
#             "-",
#             "ShowBlocks",
#             "Maximize",
#         ],
#     },
# ]


# from ckeditor.configs import DEFAULT_CONFIG

# CKEDITOR_CONFIGS = {
#     # "default": DEFAULT_CONFIG,
#     "content-custom-toolbar": {
#         "width": "100%",
#         "height": "500px",
#         "skin": "moono-lisa",
#         "toolbar": CUSTOM_TOOLBAR,
#         "toolbarGroups": None,
#         "extraPlugins": ",".join(["image2", "codesnippet"]),
#         "removePlugins": ",".join(["image"]),
#         "codeSnippet_theme": "xcode",
#     },
#     "comment-custom-toolbar": {
#         "width": "100%",
#         "height": "100px",
#         "fontSize_defaultLabel": "16px",
#         "skin": "moono-lisa",
#         "toolbar": [
#             {
#                 "name": "document",
#                 "items": [
#
#                 ],
#             },
#             {
#                 "name": "widgets",
#                 "items": [
#                     "Styles",
#                     "Format",
#                     'Font',
#                     'FontSize',
#                     "TextColor",
#                     "BGColor",
#                     "CodeSnippet",
#                     "Smiley",
#                     "ShowBlocks",
#                     "Maximize",
#                 ],
#             }
#         ],
#         "toolbarGroups": None,
#         "extraPlugins": "codesnippet",
#         # "removePlugins": ",".join(["image"]),
#         "codeSnippet_theme": "xcode",
#     },
# }
# ckeditor 结束 ######################################################

# 每页评论的数量
COMMENT_PAGE_SIZE = 3

# mdeditor 开始
MDEDITOR_CONFIGS = {
    'default': {
        'width': '100%',  # 自定义编辑框宽度
        'height': 500,  # 自定义编辑框高度
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
        'height': 200,  # 自定义编辑框高度
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
}
