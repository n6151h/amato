
from django.shortcuts import render

from rest_framework import viewsets

from .models import *

from .serializers import *

class SingerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "singers" to be viewed or edited.
    """
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class InstrumentalistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows instrumentalists to be viewed or edited.
    """
    queryset = Instrumentalist.objects.all()
    serializer_class = InstrumentalistSerializer

class DancerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "dancers" to be viewed or edited.
    """
    queryset = Dancer.objects.all()
    serializer_class = DancerSerializer

class StaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "singers" to be viewed or edited.
    """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

