from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ExperimentViewSet


router = DefaultRouter()
router.register('experiments', ExperimentViewSet, basename='experiment')
router.register('events', EventViewSet, basename='event')

urlpatterns = router.urls
