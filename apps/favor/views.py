from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ratelimit.decorators import ratelimit

from .forms import FavorForm
from .models import Favor


@ratelimit(key='ip', rate='2/s', block=True)
@login_required(login_url='/accounts/login/')
def favor_view(request):
    if request.htmx:

        print('request.htmx')
        form = FavorForm(request.POST or None)

        if form.is_valid():

            object_id = form.cleaned_data.get('object_id')
            content_type_id = form.cleaned_data.get('content_type_id')

            favor = Favor.objects.filter(
                object_id=object_id,
                content_type_id=content_type_id,
                author=request.user).first()
            if favor:
                favor.delete()
                is_favor = False
            else:
                Favor.objects.create(
                    object_id=object_id,
                    content_type_id=content_type_id,
                    author=request.user)
                is_favor = True
            print(is_favor)
            return render(request,
                          'snippet/htmx/star_form.html',
                          context={
                              "is_favor": is_favor,
                              # "object_id": object_id,
                              # "content_type_id": content_type_id,
                          })
        else:
            return HttpResponse(str(form.errors) + '字段出错了')

    if request.method == "POST":
        form = FavorForm(request.POST or None)

        if form.is_valid():

            object_id = form.cleaned_data.get('object_id')
            content_type_id = form.cleaned_data.get('content_type_id')

            favor = Favor.objects.filter(
                object_id=object_id,
                content_type_id=content_type_id,
                author=request.user).first()
            if favor:
                favor.delete()
            else:
                Favor.objects.create(
                    object_id=object_id,
                    content_type_id=content_type_id,
                    author=request.user)

            return redirect(f'/snippet/article/{object_id}')
        else:
            return HttpResponse(str(form.errors) + '字段出错了')
    else:
        return redirect(f'/snippet/article/')
