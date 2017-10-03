
from django.shortcuts import render

from rest_framework import viewsets

from .models import *

from .serializers import *

class ContactDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contact data to be viewed or edited.
    """
    queryset = ContactData.objects.all()
    serializer_class = ContactDataSerializer


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


class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def perform_create(self, serializer):
        # If we're using Hyperlinked views, we need to
        # parse the URL we get and then resolve the path
        # to come up with the book.
        parts = urlparse(self.request.data.get('book'))
        book = Book.objects.get(pk=resolve(parts.path).kwargs['pk'])

        # Otherwise, we can just get it using the "book" element
        # of request.data directly ...
        #book = Book.objects.get(pk=self.request.data['book'])

        serializer.save(book=book)
