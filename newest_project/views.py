from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic import FormView
from newest_project.forms import NameForm
from information.models import *
from django.views.generic import CreateView
from django.views.generic import ListView



class FillOut(FormView):
    template_name = "form.html"
    form_class = NameForm
    success_url = "thanks/"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class Home(TemplateView):
    template_name = "index.html"

class AboutUs(TemplateView):
    template_name = "aboutus.html"
    # FACE BOOK MAKING A POST



class PostCreateView(CreateView):
    template_name = "form.html"
    fields = ['content']
    model = Posts
    success_url = "/listpost"

class PostListView(ListView):
    template_name = "list.html"
    model = Posts

class PostDetailView():
    template_name = "detail.html"
    model = Posts


class UpVoteView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        print(self.kwargs['pk'])
        post = Posts.objects.get(pk = self.kwargs['pk'])
        try:
            post.view_counter += 1
        except Exception as e:
            print('Error:' + e)
            post.view_counter = 0
        post.save()
        return('/listpost')
