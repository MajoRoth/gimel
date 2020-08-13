from django.views.generic import CreateView, TemplateView
from Orders.models import Worder, Aorder, Torder
from django.http import HttpResponseRedirect
from django.urls import reverse
from Orders import forms



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
    form_class = forms.WorderFrom
    model = Worder
    template_name = 'Order/worder_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TorderCreateView(CreateView):
    template_name = 'Order/torder_form.html'
    form_class = forms.TorderFrom
    model = Torder

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AorderCreateView(CreateView):
    template_name = 'Order/aorder_form.html'
    form_class = forms.AorderFrom
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

class TorderAdmin(TemplateView):
    template_name = 'Order/Torder_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Torders'] = Torder.objects.all()
        return context

class AorderAdmin(TemplateView):
    template_name = 'Order/Aorder_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Aorders'] = Aorder.objects.all()
        return context


"""
    Approval methods - function views:
"""


def approveWorder(request, order_pk):
    order = Worder.objects.get(pk=order_pk)
    order.approve()
    return HttpResponseRedirect(reverse('Orders:worderadmin'))


def disapproveWorder(request, order_pk):
    order = Worder.objects.get(pk=order_pk)
    order.disapprove()
    return HttpResponseRedirect(reverse('Orders:worderadmin'))


def approveTorder(request, order_pk):
    order = Torder.objects.get(pk=order_pk)
    order.approve()
    return HttpResponseRedirect(reverse('Orders:torderadmin'))


def disapproveTorder(request, order_pk):
    order = Torder.objects.get(pk=order_pk)
    order.disapprove()
    return HttpResponseRedirect(reverse('Orders:torderadmin'))


def approveAorder(request, order_pk):
    order = Aorder.objects.get(pk=order_pk)
    order.approve()
    return HttpResponseRedirect(reverse('Orders:aorderadmin'))


def disapproveAorder(request, order_pk):
    order = Aorder.objects.get(pk=order_pk)
    order.disapprove()
    return HttpResponseRedirect(reverse('Orders:aorderadmin'))






