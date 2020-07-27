from django.db import models


class Event(models.Model):
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=255)

    class Meta:
        abstract = True


class CameraEvent(Event):
    pass


class PlayerEvent(Event):
    pass


class DrtEvent(Event):
    pass
