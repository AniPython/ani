from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import UpdateView, DeleteView

from .forms import CreateCommentForm
from .models import Comment


@login_required
def create_comment_view(request):
    if request.method == "POST":
        form = CreateCommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save()
            return redirect(f'/snippet/article/{comment.object_id}')
        else:
            return HttpResponse(str(form.errors))


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name_suffix = '_update_form'  # 自动找 article_update_form.html
    form_class = CreateCommentForm


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name_suffix = '_delete_form'

    def get_success_url(self):
        return self.object.get_father().get_absolute_url()



