
from django.shortcuts import render

from rest_framework import viewsets

from .models import *

from .serializers import *

class SeasonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "seasons" to be viewed or edited.
    """
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class ProductionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "productions" to be viewed or edited.
    """
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

class ShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "shows" to be viewed or edited.
    """
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class CallViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows "calls" to be viewed or edited.
    """
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class CastingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows casts to be viewed or edited
    """
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer
