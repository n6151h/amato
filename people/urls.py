from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'singer', views.SingerViewSet)
router.register(r'instrument', views.InstrumentalistViewSet, "instrument")
router.register(r'dancer', views.DancerViewSet)
router.register(r'staff', views.StaffViewSet)

#router.register(r'role', views.RoleViewSet)
#router.register(r'operaticrole', views.OperaticRoleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]