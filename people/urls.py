from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = "people"

router = routers.DefaultRouter()

router.register(r'person', views.PersonViewSet)
router.register(r'artist', views.ArtistViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'contactdata', views.ContactDataViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]