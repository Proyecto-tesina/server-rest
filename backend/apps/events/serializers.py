from rest_framework.serializers import ModelSerializer

from .models import CameraEvent, DrtEvent, PlayerEvent


class CameraEventSerializer(ModelSerializer):
    class Meta:
        model = CameraEvent
        fields = ['timestamp', 'status']


class DrtEventSerializer(ModelSerializer):
    class Meta:
        model = DrtEvent
        fields = ['timestamp', 'status']


class PlayerEventSerializer(ModelSerializer):
    class Meta:
        model = PlayerEvent
        fields = ['timestamp', 'status']
