from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'News/index.html'

