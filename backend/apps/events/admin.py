from django.contrib import admin
from .models import CameraEvent, PlayerEvent, DrtEvent

admin.site.register(CameraEvent)
admin.site.register(PlayerEvent)
admin.site.register(DrtEvent)
