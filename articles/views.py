from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from news. models import Post
from. forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticlesList(ListView):
    model = Post
    ordering = '-add_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10
    queryset = Post.objects.filter(pole_ar_ne='AR')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context




class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    context_object_name = 'create'
    success_url = '/articles/'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path =='/articles/create/':
            post.pole_ar_ne = 'AR'
        post.save()
        return super().form_valid(form)


class ArticlesEdit(UpdateView, LoginRequiredMixin, TemplateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    context_object_name = 'edit'
    success_url = '/articles/'

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    context_object_name = 'delete'
    success_url = '/articles/'