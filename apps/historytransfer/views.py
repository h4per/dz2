from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.historytransfer.models import HistoryTransfer
from apps.historytransfer.serializers import HistoryTransferSerializer

# Create your views here.
class HistoryTransferAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = HistoryTransfer.objects.all()
    serializer_class = HistoryTransferSerializer
