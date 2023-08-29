from rest_framework import serializers
from apps.historytransfer.models import HistoryTransfer

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('from_user', 'to_user', 'is_completed', 'created_at', 'amount')