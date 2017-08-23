from django.conf.urls import url, include

urlpatterns = [
    url(r'^company/', include('company.urls', namespace="company")),
    url(r'^library/', include('library.urls', namespace="library")),
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^schedule/', include('schedule.urls', namespace="schedule")),
    url(r'^talent/', include('talent.urls', namespace="talent")),
]
