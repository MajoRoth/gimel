from django.views.generic import CreateView, TemplateView
from Orders.models import Worder, Aorder, Torder
from django.http import HttpResponseRedirect
from django.urls import reverse
from Orders import forms
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.utils import timezone


# Create your views here.
class OrderIndexView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'Order/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Worders'] = Worder.objects.filter(user=self.request.user).filter(Active=True)
        context['Torders'] = Torder.objects.filter(user=self.request.user).filter(Active=True).filter(date__gte=timezone.now())
        context['Aorders'] = Aorder.objects.filter(user=self.request.user).filter(Active=True).filter(date__gte=timezone.now())
        return context


class WorderCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    form_class = forms.WorderFrom
    model = Worder
    template_name = 'Order/worder_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TorderCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'Order/torder_form.html'
    form_class = forms.TorderFrom
    model = Torder

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AorderCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'Order/aorder_form.html'
    form_class = forms.AorderFrom
    model = Aorder

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorderAdmin(PermissionRequiredMixin, TemplateView):
    permission_required = 'Orders.view_worder'
    template_name = 'Order/Worder_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Worders'] = Worder.objects.filter(Active=True).order_by('date')
        return context


class TorderAdmin(PermissionRequiredMixin, TemplateView):
    permission_required = 'Orders.view_torder'
    template_name = 'Order/Torder_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Torders'] = Torder.objects.order_by('date')
        return context


class AorderAdmin(PermissionRequiredMixin, TemplateView):
    permission_required = 'Orders.view_aorder'
    template_name = 'Order/Aorder_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Aorders'] = Aorder.objects.order_by('date')
        return context


"""
    Approval methods - function views:
"""

#Worder
@permission_required('Orders.change_worder')
def approveWorder(request, order_pk):
    order = Worder.objects.get(pk=order_pk)
    order.approve()
    return HttpResponseRedirect(reverse('Orders:worderadmin'))

@permission_required('Orders.change_worder')
def collectWorder(request, order_pk):
    order = Worder.objects.get(pk=order_pk)
    order.collect()
    return HttpResponseRedirect(reverse('Orders:worderadmin'))

@permission_required('Orders.change_worder')
def returnWorder(request, order_pk):
    order = Worder.objects.get(pk=order_pk)
    order.returned()
    return HttpResponseRedirect(reverse('Orders:worderadmin'))


@permission_required('Orders.change_worder')
def disapproveWorder(request, order_pk):
    order = Worder.objects.get(pk=order_pk)
    order.disapprove()
    return HttpResponseRedirect(reverse('Orders:worderadmin'))


@login_required()
def deleteWorder(request, order_pk):
    order = Worder.objects.get(pk=order_pk)
    if order.collected:
        return HttpResponseRedirect(reverse('Orders:index'))
    order.deleted()
    return HttpResponseRedirect(reverse('Orders:index'))


#Torder
@permission_required('Orders.change_torder')
def approveTorder(request, order_pk):
    order = Torder.objects.get(pk=order_pk)
    order.approve()
    return HttpResponseRedirect(reverse('Orders:torderadmin'))


@permission_required('Orders.change_torder')
def disapproveTorder(request, order_pk):
    order = Torder.objects.get(pk=order_pk)
    order.disapprove()
    return HttpResponseRedirect(reverse('Orders:torderadmin'))


@login_required()
def deleteTorder(request, order_pk):
    order = Torder.objects.get(pk=order_pk)
    order.delete()
    return HttpResponseRedirect(reverse('Orders:index'))


# Aorder
@permission_required('Orders.change_aorder')
def approveAorder(request, order_pk):
    order = Aorder.objects.get(pk=order_pk)
    order.approve()
    return HttpResponseRedirect(reverse('Orders:aorderadmin'))


@permission_required('Orders.change_aorder')
def disapproveAorder(request, order_pk):
    order = Aorder.objects.get(pk=order_pk)
    order.disapprove()
    return HttpResponseRedirect(reverse('Orders:aorderadmin'))


@login_required()
def deleteAorder(request, order_pk):
    order = Aorder.objects.get(pk=order_pk)
    order.delete()
    return HttpResponseRedirect(reverse('Orders:index'))






