from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress')
        

class UserRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=100, write_only=True
    )
    confirm_phone_number = serializers.CharField(
        max_length=100, write_only=True
    )
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone_number', 'confirm_phone_number')

    def validate(self, attrs):
        if attrs['phone_number'] != attrs['confirm_phone_number']:
            raise serializers.ValidationError({'phone_number':'Номера отличаются'})
        elif '+997' in attrs['phone_number'] and '+998' in attrs['phone_number'] and '+7' in attrs['phone_number']:
            raise serializers.ValidationError({'phone_number':'Введённый номер не соответсвует стандартам КР (+996)'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['user_name'],
        )
        user.set_password(validated_data['phone_number'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress')
