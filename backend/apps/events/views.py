from rest_framework import viewsets

from .models import CameraEvent, DrtEvent, PlayerEvent

from .serializers import CameraEventSerializer, DrtEventSerializer
from .serializers import PlayerEventSerializer


class CameraEventViewSet(viewsets.ModelViewSet):

    queryset = CameraEvent.objects.all()
    serializer_class = CameraEventSerializer


class DrtEventViewSet(viewsets.ModelViewSet):

    queryset = DrtEvent.objects.all()
    serializer_class = DrtEventSerializer


class PlayerEventViewSet(viewsets.ModelViewSet):

    queryset = PlayerEvent.objects.all()
    serializer_class = PlayerEventSerializer
