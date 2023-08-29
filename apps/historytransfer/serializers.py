from rest_framework import serializers
from apps.historytransfer.models import HistoryTransfer
from apps.users.serializers import UserSerializer

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('from_user', 'to_user', 'is_completed', 'created_at', 'amount')


class HistoryTransferDetailSerializer(serializers.ModelSerializer):
    user_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = HistoryTransfer
        fields = ('from_user', 'to_user', 'is_completed', 'created_at', 'amount', 'user_users')