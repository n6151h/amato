
from django.shortcuts import render

from rest_framework import viewsets

from .models import *

from .serializers import *

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "books" (scripts, scores) to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer