from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.serializers import UserSerializer, ProfileSerializer
from users.models import MainUser, Profile


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        print(self.request.user)
        return MainUser.objects.all()


class ProfileView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




    