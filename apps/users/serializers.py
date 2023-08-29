from rest_framework import serializers
from apps.users.models import User
from apps.historytransfer.serializers import HistoryTransferSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=100, write_only=True
    )
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone_number', 'age')

    def validate(self, attrs):
        if attrs['phone_number'] != '+996':
            raise serializers.ValidationError({'phone_number':'Введённый номер не соответсвует стандартам КР (+996)'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            user_name=validated_data['user_name']
        )
        user.set_password(validated_data['phone_number'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    user_transfers = HistoryTransferSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress', 'user_transfers')
