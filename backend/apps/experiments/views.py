from django.utils import timezone

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event, Experiment

from .serializers import EventSerializer, ExperimentSerializer


class ExperimentViewSet(viewsets.ModelViewSet):

    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

    @action(detail=True, methods=['patch'])
    def start(self, request, pk):
        experiment = self.get_object()

        serializer = ExperimentSerializer(
            experiment,
            data={'started_at': timezone.now()},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    @action(detail=True, methods=['patch'])
    def end(self, request, pk):
        experiment = self.get_object()

        serializer = ExperimentSerializer(
            experiment,
            data={'ended_at': timezone.now()},
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    @action(detail=False, methods=['GET'])
    def last(self, request):
        experiment = Experiment.objects.first()
        serializer = ExperimentSerializer(experiment)
        return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
