from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ratelimit.decorators import ratelimit

from .forms import FavorForm
from .models import Favor


@ratelimit(key='ip', rate='1/s', block=True)
@login_required(login_url='/accounts/login/')
def favor_view(request):
    if request.htmx:

        form = FavorForm(request.POST or None)

        if form.is_valid():

            object_id = form.cleaned_data.get('object_id')
            content_type = form.cleaned_data.get('content_type')

            favor = Favor.objects.filter(
                object_id=object_id,
                content_type=content_type,
                author=request.user).first()
            if favor:
                favor.delete()
                is_favor = False
            else:
                Favor.objects.create(
                    object_id=object_id,
                    content_type=content_type,
                    author=request.user)
                is_favor = True

            return render(request,
                          'snippet/htmx/star_form.html',
                          context={"is_favor": is_favor})
        else:
            return HttpResponse(str(form.errors) + '字段出错了')

