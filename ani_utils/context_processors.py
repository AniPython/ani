def get_is_active(request):
    context = {}

    sp = request.path.split('/')

    # 导航标签高亮
    if len(sp) > 1:
        context['is_active'] = sp[1]

    # 爬虫页标签高亮
    if len(sp) > 2:
        context['crawler_is_active'] = sp[2]

    # 代码片段页标签高亮
    if request.path == '/snippet/article/':
        context['snippet_tag_is_active'] = request.GET.get('tag', 'all')

    return context
