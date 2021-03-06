import markdown.extensions.fenced_code
from datetime import datetime
from django.utils.timezone import now as now_func, localtime
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def convert_markdown(value):
    return markdown.markdown(
        value,
        # https://python-markdown.github.io/extensions/#officially-supported-extensions
        extensions=[
            'fenced_code',  # 显示代码
            'nl2br',        # 换行
            'sane_lists',    # list
            'tables',    # list
            'md_in_html',
        ]
    )

# encoding: utf-8
# from django import template


# register = template.Library()


@register.filter
def time_since(value):
    """
    time距离现在的时间间隔
    1.如果时间间隔小于1分钟以内，那么就显示“刚刚”
    2.如果是大于1分钟小于1小时，那么就显示“xx分钟前”
    3.如果是大于1小时小于24小时，那么就显示“xx小时前”
    4.如果是大于24小时小于30天以内，那么就显示“xx天前”
    5.否则就是显示具体的时间
    2017/10/20 16:15
    """
    if not isinstance(value, datetime):
        return value
    now = now_func()
    # timedelay.total_seconds
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif 60 <= timestamp < 60 * 60:
        minutes = int(timestamp / 60)
        return '%s分钟前' % minutes
    elif 60 * 60 <= timestamp < 60 * 60 * 24:
        hours = int(timestamp / 60 / 60)
        return '%s小时前' % hours
    elif 60 * 60 * 24 <= timestamp < 60 * 60 * 24 * 30:
        days = int(timestamp / 60 / 60 / 24)
        return '%s天前' % days
    else:
        return value.strftime("%Y/%m/%d %H:%M")


@register.filter
def time_format(value):
    if not isinstance(value, datetime):
        return value

    return localtime(value).strftime("%Y/%m/%d %H:%M:%S")
