from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ExperimentViewSet, LauncherView


router = DefaultRouter()
router.register('experiments', ExperimentViewSet, basename='experiment')
router.register('events', EventViewSet, basename='event')

urlpatterns = [
    path('launch-simulation', LauncherView.as_view()),
]
urlpatterns += router.urls
