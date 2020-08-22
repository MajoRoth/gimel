from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from website import forms
from Scripts.scripts import send_mail
from django.shortcuts import render

class MoralsPage(TemplateView):
    template_name = "morals.html"

class JingelsPage(TemplateView):
    template_name = "jingels.html"


def home(request):
    form = forms.ContactForm()
    if request.method == 'GET':
        return render(request, 'index.html', {'form': form})

    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd.get('name'),
                      cd.get('phone'),
                      cd.get('email'),
                      cd.get('message'))
            return render(request, 'index.html', {'form': form})




