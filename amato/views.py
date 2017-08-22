from django.conf.urls import url
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"

