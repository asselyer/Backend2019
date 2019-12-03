from rest_framework import generics
from rest_framework import mixins

from api.models import Blog, BlogCategory, Post, PostComment, PostFile, FavoritePost
from api.serializers import BlogCategorySerializer, FavoritePostSerializer, BlogSerializer, PostChangeSerializer, PostShortSerializer, PostFullSerializer, PostCommentSerializer, PostMediaSerializer



class PostMediafileCreateView(generics.CreateAPIView):
    queryset = PostFile.objects.all()
    serializer_class = PostMediaSerializer


class PostCommentCreateView(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
