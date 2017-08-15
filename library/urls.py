from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from . import views

router = routers.DefaultRouter()

schema_view = get_schema_view(title='Pastebin API')

router.register(r'book', views.BookViewSet)
router.register(r'musical', views.MusicalViewSet)
router.register(r'script', views.ScriptViewSet)
router.register(r'opera', views.OperaViewSet)

#router.register(r'role', views.RoleViewSet)
#router.register(r'operaticrole', views.OperaticRoleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
]

