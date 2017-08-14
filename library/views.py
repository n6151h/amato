from django.shortcuts import render

from rest_framework import viewsets

from .models import Opera, OperaticRole

from .serializers import OperaSerializer, OperaticRoleSerializer

class OperaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows opera scores to be viewed or edited.
    """
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer


class OperaticRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows operatic roles to be viewed or edited.
    """
    queryset = OperaticRole.objects.all()
    serializer_class = OperaticRoleSerializer
