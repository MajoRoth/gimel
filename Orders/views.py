from django.shortcuts import render
from django.views.generic import CreateView
from Orders.models import Worder, Torder, Aorder
# Create your views here.

class WorderCreateView(CreateView):
    fields = ('description', 'date')
    model = Worder
    template_name = 'Order/worder_form.html'



"""
class TorderCreateView(CreateView):
    fields = ('description', 'date')
    model = Torder




class AorderCreateView(CreateView):
    fields = ('area', 'date')
    model = Aorder

"""


