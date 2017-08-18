from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'talent', views.TalentViewSet)
router.register(r'singing', views.SingingViewSet)
router.register(r'dancing', views.DancingViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]