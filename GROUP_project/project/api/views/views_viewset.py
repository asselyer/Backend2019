import logging
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from django.http import Http404
from django.shortcuts import get_object_or_404

from api.models import Project, Task, Block, TaskComment
from api.serializers import ProjectSerializer, TaskShortSerializer, TaskFullSerializer, TaskChangeSerializer, SetExecutorSerializer, BlockSerializer, TaskCommentSerializer, ProjectSerializer2

from api.constants import TASK_TODO
from api.permissions import IsDeveloperPermission, CanCreateProjectPermission

logger = logging.getLogger(__name__)


class ProjectListViewSet(mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer2
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)
    
    @action(methods=['GET'], detail=False)
    def my(self, request):
        projects = Project.objects.filter(creator=self.request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def tasks(self, request, pk):
        instance = self.get_object()
        serializer = TaskShortSerializer(instance.tasks, many=True, context={
            'request': self.request
        })
        return Response(serializer.data)



class TaskViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskFullSerializer
        if self.action == 'set_executor':
            return SetExecutorSerializer
        if self.action in ['create', 'update']:
            return TaskChangeSerializer
        if self.action == 'list':
            return TaskFullSerializer    
        # if self.action in ['destroy']:
        #     return TaskChangeSerializer

    @action(methods=['PUT'], detail=True)
    def set_executor(self, request, pk):
        instance = self.get_object()
        instance.set_executor(request.data.get('executor_id'))
        serializer = self.get_serializer(instance)
        logger.info(f"{self.request.user} set as executor id: {request.data.get('executor_id')}")
        return Response(serializer.data)

    
    # def perform_destroy(self, instance):
    #     instance.delete(save=False)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
        
    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
    #     logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
    #     logger.warning(f"{self.request.user} created task: {serializer.data.get('name')}")
    #     logger.error(f"{self.request.user} created task: {serializer.data.get('name')}")
    #     logger.critical(f"{self.request.user} created task: {serializer.data.get('name')}")

class BlockListViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class BlockDetailViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

