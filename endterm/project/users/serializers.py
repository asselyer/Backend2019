from rest_framework import serializers
from users.models import MainUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name',  'password')

   