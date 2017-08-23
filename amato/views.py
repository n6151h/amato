from django.conf.urls import url
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"


class HomeView(TemplateView):
    template_name = "home.html"


class PeopleView(TemplateView):
    template_name = "people.html"

class TalentsView(TemplateView):
    template_name = "talents.html"

class ScheduleView(TemplateView):
    template_name = "schedule.html"


