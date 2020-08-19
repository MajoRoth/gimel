from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"

class MoralsPage(TemplateView):
    template_name = "morals.html"