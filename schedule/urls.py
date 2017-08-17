from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from . import views

router = routers.DefaultRouter()

router.register(r'season', views.SeasonViewSet)
router.register(r'production', views.ProductionViewSet)
router.register(r'show', views.ShowViewSet)
router.register(r'call', views.CallViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
