from django import forms
from django.views.generic import CreateView, TemplateView
from Orders.models import Worder, Aorder, Torder


# Create your views here.


class OrderIndexView(TemplateView):
    template_name = 'Order/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Worders'] = Worder.objects.filter(user=self.request.user)
        context['Torders'] = Torder.objects.filter(user=self.request.user)
        context['Aorders'] = Aorder.objects.filter(user=self.request.user)
        return context


class WorderCreateView(CreateView):
    fields = ('description', 'date')
    model = Worder
    template_name = 'Order/worder_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TorderCreateView(CreateView):
    template_name = 'Order/torder_form.html'
    fields = ('description', 'date')
    model = Torder

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AorderCreateView(CreateView):
    template_name = 'Order/aorder_form.html'
    fields = ('area', 'date')
    model = Aorder

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorderAdmin(TemplateView):
    template_name = 'Order/Worder_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Worders'] = Worder.objects.all()
        return context


def approveOrder(request, **kwargs):
    Worder.approve(self=Worder.objects.get(id=kwargs['pk']))
    return WorderAdmin




