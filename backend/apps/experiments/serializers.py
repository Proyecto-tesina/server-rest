from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Event, Experiment


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ExperimentSerializer(ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Experiment
        fields = '__all__'

    def validate(self, data):

        start_date = self._get_value(data, 'started_at')
        end_date = self._get_value(data, 'ended_at')

        if end_date and not start_date:
            raise ValidationError(
                "Start date should be specified if end date was specified")

        if start_date and end_date and start_date > end_date:
            raise ValidationError("Start date should be before to end date")

        return data

    def _get_value(self, data, key):
        if self.partial and key not in data.keys():
            return getattr(self.instance, key)
        else:
            return data.get(key)
