from django.shortcuts import render
from rest_framework import generics
from api.serializers import ProjectSerializer, ProjectSerializer2, TaskSerializer, TaskSerializer2, BlockSerializer
from api.models import Project, Task, Block

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