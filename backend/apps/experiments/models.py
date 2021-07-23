from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


EVENT_NAMES = (("CAMERA", "Camera"), ("PLAYER", "Player"), ("DRT", "Drt"))


class Experiment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, unique=True)

    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Experiment - {self.created_at}"

    def clean(self):
        super().clean()

        if not self.started_at and self.ended_at:
            raise ValidationError(
                "Started_at should be specified if ended_at was specified"
            )

        if self.started_at and self.ended_at and self._date_range_invalid():
            raise ValidationError("Started_at should be before to ended_at")

    def _date_range_invalid(self):
        return self.started_at > self.ended_at

    def start(self):
        self.started_at = timezone.now()

    def end(self):
        self.ended_at = timezone.now()


class Event(models.Model):
    name = models.CharField(max_length=255, choices=EVENT_NAMES)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=255)

    experiment = models.ForeignKey(
        Experiment, on_delete=models.CASCADE, related_name="events"
    )

    def __str__(self):
        return f"{self.name} - {self.timestamp}"
