import logging
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from django.http import Http404
from django.shortcuts import get_object_or_404

from api.models import Article, FavoriteArticle
from api.serializers import ArticleSerializer, ArticleShortSerializer, ArticleFullSerializer, ArticleFavSerializer,  ArticleSerializer


logger = logging.getLogger(__name__)

class ArticleViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleShortSerializer
        if self.action == 'retrieve':
            return ArticleFullSerializer
        if self.action == 'favorite':
            return ArticleFavSerializer
        if self.action in ['create', 'update']:
            return ArticleSerializer
    
    def perform_create(self, serializer):
        permission_classes = (IsAuthenticated,)
        return serializer.save(creator=self.request.user)
    
    @action(methods=['POST'], detail=False)
    def favorite(self, request):
        articles = FavoriteArticle.objects.filter(user=self.request.user)
        serializer = self.get_serializer(articles, many=True)
        return serializer.save(user=self.request.user)

    # @action(methods=['GET'], detail=True)
    # def tasks(self, request, pk):
    #     instance = self.get_object()
    #     serializer = TaskShortSerializer(instance.tasks, many=True, context={
    #         'request': self.request
    #     })
    #     return Response(serializer.data)