from rest_framework import validators
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Event, Experiment


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

        validators = [
            validators.UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=["experiment", "name", "timestamp"],
                message="Experiment, event name and timestamp are unique together",
            )
        ]


class ExperimentSerializer(ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Experiment
        fields = "__all__"

    def validate(self, data):
        start_date = self._get_value(data, "started_at")
        end_date = self._get_value(data, "ended_at")

        if end_date and not start_date:
            raise ValidationError(
                "If end_date was supplied, start date must be specified"
            )

        if start_date and end_date and start_date > end_date:
            raise ValidationError("Start date must be previous to end date")

        return data

    def _get_value(self, data, key):
        if self.partial and key not in data.keys():
            return getattr(self.instance, key)
        else:
            return data.get(key)
