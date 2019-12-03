import logging
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from django.http import Http404
from django.shortcuts import get_object_or_404

from api.models import Blog, BlogCategory, Post, PostComment, PostFile, FavoritePost
from api.serializers import FavoritePostSerializer, BlogSerializer, PostChangeSerializer, PostShortSerializer, PostFullSerializer
from api.constants import BLOG_PUBLIC
from api.permissions import IsDeveloperPermission, CanCreateProjectPermission

logger = logging.getLogger(__name__)


class FavoritePostsViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = FavoritePost.objects.all()
    serializer_class = FavoritePostSerializer


class FavoritePostsDetailViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = FavoritePost.objects.all()
    serializer_class = FavoritePostSerializer


class BlogViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)
    
    @action(methods=['GET'], detail=False)
    def my(self, request):
        blogs = Blog.objects.filter(creator=self.request.user)
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def posts(self, request, pk):
        instance = self.get_object()
        serializer = PostShortSerializer(instance.posts, many=True, context={
            'request': self.request
        })
        return Response(serializer.data)



class PostViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostFullSerializer
        # if self.action == 'set_executor':
        #     return SetExecutorSerializer
        if self.action in ['create', 'update']:
            return PostChangeSerializer
        if self.action == 'list':
            return PostShortSerializer    
        # if self.action in ['destroy']:
        #     return TaskChangeSerializer

    # @action(methods=['PUT'], detail=True)
    # def set_executor(self, request, pk):
    #     instance = self.get_object()
    #     instance.set_executor(request.data.get('executor_id'))
    #     serializer = self.get_serializer(instance)
    #     logger.info(f"{self.request.user} set as executor id: {request.data.get('executor_id')}")
    #     return Response(serializer.data)

    
    # def perform_destroy(self, instance):
    #     instance.delete(save=False)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created post: {serializer.data.get('title')}")
        
    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
    #     logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
    #     logger.warning(f"{self.request.user} created task: {serializer.data.get('name')}")
    #     logger.error(f"{self.request.user} created task: {serializer.data.get('name')}")
    #     logger.critical(f"{self.request.user} created task: {serializer.data.get('name')}")

# class BlockListViewSet(mixins.CreateModelMixin,
#                          mixins.ListModelMixin,
#                          viewsets.GenericViewSet):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer


# class BlockDetailViewSet(mixins.RetrieveModelMixin,
#                            mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin,
#                            viewsets.GenericViewSet):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer

