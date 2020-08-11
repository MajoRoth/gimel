from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from Orders.models import Worder, Aorder, Torder

# Create your views here.


class OrderIndexView(TemplateView):
    template_name = 'Order/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Worder.objects.filter(user=self.request.user)
        return context


class WorderCreateView(CreateView):
    fields = ('description', 'date')
    model = Worder
    template_name = 'Order/worder_form.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class TorderCreateView(CreateView):
    fields = ('description', 'date')
    model = Torder

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class AorderCreateView(CreateView):
    fields = ('area', 'date')
    model = Aorder

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


