from django.conf.urls import url, include
from rest_framework import routers

app_name = "api"

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^library/', include('library.urls', namespace="library")),
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^schedule/', include('schedule.urls', namespace="schedule")),
    url(r'^talent/', include('talent.urls', namespace="talent")),
]
