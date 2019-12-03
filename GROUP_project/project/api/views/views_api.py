from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Blog, BlogCategory, Post, PostComment, PostFile, FavoritePost
from api.serializers import BlogCategorySerializer, FavoritePostSerializer, BlogSerializer, PostChangeSerializer, PostShortSerializer, PostFullSerializer

class BlogCategoryAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BlogCategoryDetailAPIView(APIView):
    # http_method_names = ['put', 'delete']
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return BlogCategory.objects.get(pk=pk)
        except BlogCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = BlogCategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = BlogCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class TaskDocumentAPIView(APIView):
#     http_method_names = ['get','post', 'put', 'delete']

#     def get(self, request):
#         projects = TaskDocument.objects.all()
#         serializer = TaskDocumentSerializer(projects, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TaskDocumentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request):
#         pass