from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render
from rest_framework.response import Response

from api.serializers import UserSerializer, ProfileSerializer, ProjectSerializer, ProjectSerializer2, TaskSerializer, TaskSerializer2, BlockSerializer, ProjectSerializer3, ProfileSerializer1
from api.models import MainUser, Profile, Project, Task, Block


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        print(self.request.user)
        return MainUser.objects.all()

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer1
    lookup_field = 'user__username'

class ProfileEdit(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer1
    lookup_field = 'id'

class ProjectListAPIView(APIView):
    http_method_names = ['get', 'post']
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer2

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post']

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer2

class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    http_method_names = ['get', 'post']

class ProjectTasksList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Task.objects.filter(projects_id=self.kwargs["pk"])
        return queryset
    serializer_class = TaskSerializer2
