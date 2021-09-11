from pathlib import Path

from django.conf import settings
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
import re

from ratelimit.decorators import ratelimit
from django.views.generic import ListView, DetailView

from .models import LearningResources
from django.forms.models import model_to_dict

crawler_code_dir = settings.BASE_DIR / 'apps' / 'crawler' / 'code'


def crawler_index(request):
    return redirect('crawler:crawler1')


def crawler1(request):
    """
    Hello world
    """
    # 方案一的代码
    code_crawler1_1_path = crawler_code_dir / 'crawler1_1.py'
    code_crawler1_1 = open(code_crawler1_1_path).read()

    # 方案二的代码
    code_crawler1_2_path = crawler_code_dir / 'crawler1_2.py'
    code_crawler1_2 = open(code_crawler1_2_path).read()

    # 方案三的代码
    code_crawler1_3_path = crawler_code_dir / 'crawler1_3.py'
    code_crawler1_3 = open(code_crawler1_3_path).read()

    return render(
        request,
        'crawler/crawler1.html',
        context={
            'code_crawler1_1': code_crawler1_1,
            'code_crawler1_2': code_crawler1_2,
            'code_crawler1_3': code_crawler1_3,
        })


def crawler2(request):
    """
    2. 静夜思
    """
    if re.match(r'^python|^java', request.headers.get('User-Agent')):
        return HttpResponse('浏览器繁忙, 请稍后再访问')

    # 后端代码片段
    code1 = """def crawler2(request):
if re.match(r'^python|^java', request.headers.get('User-Agent')):
    return HttpResponse('浏览器繁忙, 请稍后再访问')
return render(request, 'crawler/crawler2.html')"""

    # 方案一的代码
    code_crawler2_1_path = crawler_code_dir / 'crawler2_1.py'
    code_crawler2_1 = open(code_crawler2_1_path).read()
    return render(request, 'crawler/crawler2.html',
                  context={
                      "code1": code1,
                      "code_crawler2_1": code_crawler2_1}
                  )


@ratelimit(key='ip', rate='2/s', block=True)
def crawler3(request):
    """
    3. 多页内容
    """
    poem1 = """<h4>相思</h4>
               <h6 class="text-black-50">王维</h6>
               <p>红豆生南国，</p>
               <p>春来发几枝。</p>
               <p>愿君多采撷，</p>
               <p>此物最相思。</p>"""

    poem2 = """<h4>鹿柴</h4>
               <h6 class="text-black-50">王维</h6>
               <p>空山不见人，</p>
               <p>但闻人语响。</p>
               <p>返景入深林，</p>
               <p>复照青苔上。</p>"""

    poem3 = """<h4>渭城曲 / 送元二使安西</h4>
               <h6 class="text-black-50">王维</h6>
               <p>渭城朝雨浥轻尘，</p>
               <p>客舍青青柳色新。</p>
               <p>劝君更尽一杯酒，</p>
               <p>西出阳关无故人。</p>"""
    poems = [poem1, poem2, poem3]
    page = request.GET.get('page', '1')

    # 方案一的代码
    code_crawler3_1_path = crawler_code_dir / 'crawler3_1.py'
    code_crawler3_1 = open(code_crawler3_1_path).read()

    return render(request,
                  'crawler/crawler3.html',
                  context={
                      'poem': poems[int(page) - 1],
                      "code_crawler3_1": code_crawler3_1
                  })


# crawler4
class Crawler4ListView(ListView):
    model = LearningResources
    paginate_by = 3

    template_name = 'crawler/crawler4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 方法一的代码
        code_crawler4_1_path = crawler_code_dir / 'crawler4_1.py'
        code_crawler4_1 = open(code_crawler4_1_path).read()

        # 方法二的代码
        code_crawler4_2_path = crawler_code_dir / 'crawler4_2.py'
        code_crawler4_2 = open(code_crawler4_2_path).read()

        context['code_crawler4_1'] = code_crawler4_1
        context['code_crawler4_2'] = code_crawler4_2

        return context


class Crawler4DetailView(DetailView):
    model = LearningResources
    template_name = 'crawler/crawler4_detail.html'

    def get_queryset(self):
        return LearningResources.objects.all()


def crawler5(request):
    # 方法一的代码
    code_crawler5_1_path = crawler_code_dir / 'crawler5_1.py'
    code_crawler5_1 = open(code_crawler5_1_path).read()

    return render(
        request,
        'crawler/crawler5.html',
        context={
            'code_crawler5_1': code_crawler5_1,
        }
    )


def crawler6(request):
    # 方法一的代码
    code_crawler6_1_path = crawler_code_dir / 'crawler6_1.py'
    code_crawler6_1 = open(code_crawler6_1_path).read()

    # 方法二的代码
    code_crawler6_2_path = crawler_code_dir / 'crawler6_2.py'
    code_crawler6_2 = open(code_crawler6_2_path).read()

    return render(
        request,
        'crawler/crawler6.html',
        context={
            'code_crawler6_1': code_crawler6_1,
            'code_crawler6_2': code_crawler6_2,
        }
    )


def crawler6_download_file(request):
    """
    文件下载
    """
    dir_ = Path(__file__).resolve().parent
    file = open(dir_ / 'apps.py', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="apps.py"'
    return response


def crawler7(request):
    """
    模拟登录
    """
    # 方案一的代码
    code_crawler7_1_path = crawler_code_dir / 'crawler7_1.py'
    code_crawler7_1 = open(code_crawler7_1_path).read()

    # 方案二的代码
    code_crawler7_2_path = crawler_code_dir / 'crawler7_2.py'
    code_crawler7_2 = open(code_crawler7_2_path).read()

    # 方案三的代码
    code_crawler7_3_path = crawler_code_dir / 'crawler7_3.py'
    code_crawler7_3 = open(code_crawler7_3_path).read()

    return render(
        request,
        'crawler/crawler7.html',
        context={
            'code_crawler7_1': code_crawler7_1,
            'code_crawler7_2': code_crawler7_2,
            'code_crawler7_3': code_crawler7_3,
        }
    )


def crawler8(request):
    """
    Ajax 请求
    """
    # 方案一的代码
    code_crawler8_1_path = crawler_code_dir / 'crawler8_1.py'
    code_crawler8_1 = open(code_crawler8_1_path).read()

    # 方案二的代码
    code_crawler8_2_path = crawler_code_dir / 'crawler8_2.py'
    code_crawler8_2 = open(code_crawler8_2_path).read()

    return render(
        request,
        'crawler/crawler8.html',
        context={
            'code_crawler8_1': code_crawler8_1,
            'code_crawler8_2': code_crawler8_2,
        }
    )


def crawler8_api(request):
    data = serialize('json', LearningResources.objects.all())
    # print(data)

    rows = []
    for row in LearningResources.objects.all():
        rows.append(model_to_dict(row))
    result = {
        "data": rows
    }
    return JsonResponse(result)
