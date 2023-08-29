from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress')
        

class UserRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=100, write_only=True
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'age')

    def validate(self, attrs):
        if attrs['phone_number'] != '+996':
            raise serializers.ValidationError({'phone_number':'Введённый номер не соответсвует стандартам КР (+996)'})
        return attrs
    

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress')
