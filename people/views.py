
from django.shortcuts import render

from rest_framework import viewsets

from .models import *

from .serializers import *

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artists to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    #def get_queryset(self):
    #    import pdb
    #    pdb.set_trace()

