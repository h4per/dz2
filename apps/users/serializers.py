from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress')
        

class UserRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=100, write_only=True
    )
    class Meta:
        model = User
        fields = ('name', 'email', 'phone_number', 'age')

    def validate(self, attrs):
        if attrs['phone_number'] != '+996':
            raise serializers.ValidationError({'phone_number':'Введённый номер не соответсвует стандартам КР (+996)'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            age=validated_data['age']
        )
        user.set_password(validated_data['phone_number'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'phone_number',
                  'created_at', 'age', 'wallet_adress')
