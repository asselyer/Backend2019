from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render
from rest_framework.response import Response

from api.serializers import UserSerializer, ProfileSerializer, ProjectSerializer, ProjectSerializer2, TaskSerializer, TaskSerializer2, BlockSerializer, ProjectSerializer3
from api.models import MainUser, Profile, Project, Task, Block


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

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get']

class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer2

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get']

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer2

class BlockList(generics.ListAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    http_method_names = ['get']

class ProjectTasksList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Task.objects.filter(projects_id=self.kwargs["pk"])
        return queryset
    serializer_class = TaskSerializer2
