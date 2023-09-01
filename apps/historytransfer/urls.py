from rest_framework.routers import DefaultRouter
from apps.historytransfer.views import HistoryTransferAPIViewSet
from .views import CreateTransferView
from django.urls import path

router = DefaultRouter()
router.register('historytransfer', HistoryTransferAPIViewSet, 'api_historytransfers')

urlpatterns = router.urls

urlpatterns = [
    path('transfer/', CreateTransferView.as_view(), name="transfer"),
]

urlpatterns += router.urls
