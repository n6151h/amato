from django.shortcuts import render

from rest_framework import viewsets

from .models import Opera

from .serializers import OperaSerializer

class OperaScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer
