from rest_framework import serializers
from users.models import MainUser, Profile


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
        model = Profile
        fields = ('username', 'bio', 'address',)
        read_only_fields = ('username',)
