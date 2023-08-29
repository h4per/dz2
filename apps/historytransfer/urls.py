from rest_framework.routers import DefaultRouter
from apps.historytransfer.views import HistoryTransferAPIViewSet

router = DefaultRouter()
router.register('historytransfer', HistoryTransferAPIViewSet, 'api_historytransfers')

urlpatterns = router.urls