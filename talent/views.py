from rest_framework import viewsets

from .models import *

from .serializers import *

class TalentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer

    def get_queryset(self):
        return Talent.objects.all()

class SingingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Singing.objects.all()
    serializer_class =SingingSerializer


class DancingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Dancing.objects.all()
    serializer_class = DancingSerializer

