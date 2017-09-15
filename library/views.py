from django.shortcuts import render
from django.core.urlresolvers import resolve

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

from rest_framework import viewsets

from .models import *

from .serializers import *

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "books" (scripts, scores) to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ScriptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows scripts to be viewed or edited.
    """
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer


class MusicalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows musical scores to be viewed or edited.
    """
    queryset = Musical.objects.all()
    serializer_class = MusicalSerializer


class OperaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows opera scores to be viewed or edited.
    """
    queryset = Opera.objects.all()
    serializer_class = OperaSerializer


