from rest_framework import serializers
from api.models import MainUser, UserProfile, Product, Service, ProductServiceBase


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = MainUser.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    address = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = ('username', 'bio', 'address')

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        # fields = ('id', 'name', 'price', 'description', 'created_at')
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Service
        # fields = ('id', 'name', 'price', 'description', 'created_at')
        fields = '__all__'

    def validate_dur(self, value):
        if 20 < value > 50:
            raise serializers.ValidationError('status options: [1, 2, 3]')
        return value

class ProductServiceShortSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductServiceBase
        fields = ('id', 'name')