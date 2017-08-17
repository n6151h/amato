from django.shortcuts import render

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


class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def perform_create(self, serializer):
        serializer.save(book, self.request.book)

class OperaticRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows operatic roles to be viewed or edited.
    """
    queryset = OperaticRole.objects.all()
    serializer_class = OperaticRoleSerializer

    def perform_create(self, serializer):
        opera = Opera.objects.get(pk=self.request.data['book'])
        serializer.save(book=opera)