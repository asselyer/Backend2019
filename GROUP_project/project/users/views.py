from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer, ProfileSerializer1
from users.models import MainUser, Profile


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MainUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer1
    lookup_field = 'user__username'

class ProfileEdit(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer1
    lookup_field = 'id'