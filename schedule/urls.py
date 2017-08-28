from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = "schedule"

router = routers.DefaultRouter()

router.register(r'season', views.SeasonViewSet)
router.register(r'production', views.ProductionViewSet)
router.register(r'show', views.ShowViewSet)
router.register(r'call', views.CallViewSet)
router.register(r'casting', views.CastingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
