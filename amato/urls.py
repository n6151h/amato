"""amato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^company/', include('company.urls', namespace="company")),
    url(r'^library/', include('library.urls', namespace="library")),
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^schedule/', include('schedule.urls', namespace="schedule")),
    url(r'^talent/', include('talent.urls', namespace="talent")),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/', schema_view),

    url(r'^about', views.AboutView.as_view() )
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns