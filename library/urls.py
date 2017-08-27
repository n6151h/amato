from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = "library"

router = routers.DefaultRouter()

router.register(r'book', views.BookViewSet)
router.register(r'musical', views.MusicalViewSet)
router.register(r'script', views.ScriptViewSet)
router.register(r'opera', views.OperaViewSet)

router.register(r'role', views.RoleViewSet)
router.register(r'operaticrole', views.OperaticRoleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   url(r'^', include(router.urls)),
]

