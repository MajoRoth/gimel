from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from News import forms, models

# Create your views here.


class Index(TemplateView):
    template_name = 'News/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['News'] = models.News.objects.order_by('-pub_date')
        return context


class CreateNews(PermissionRequiredMixin, CreateView):
    permission_required = 'News.add_news'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    form_class = forms.NewsForm
    model = models.News
    template_name = 'News/create_news.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

