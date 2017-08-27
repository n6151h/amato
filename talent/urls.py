from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = "talent"

router = routers.DefaultRouter()

router.register(r'talent', views.TalentViewSet, "talent")
router.register(r'singing', views.SingingViewSet, "singing")
router.register(r'dancing', views.DancingViewSet, "dancing")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]