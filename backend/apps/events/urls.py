from rest_framework.routers import DefaultRouter
from .views import CameraEventViewSet, DrtEventViewSet, PlayerEventViewSet

router = DefaultRouter()
router.register('camera', CameraEventViewSet, basename='camera')
router.register('drt', DrtEventViewSet, basename='drt')
router.register('player', PlayerEventViewSet, basename='player')

urlpatterns = router.urls
