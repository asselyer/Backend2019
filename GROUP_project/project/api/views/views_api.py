from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Project, TaskDocument, TaskComment
from api.serializers import ProjectSerializer, TaskDocumentSerializer, TaskCommentSerializer


class TaskCommentAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        projects = TaskComment.objects.all()
        serializer = TaskCommentSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TaskDocumentAPIView(APIView):
    http_method_names = ['get','post', 'put', 'delete']

    def get(self, request):
        projects = TaskDocument.objects.all()
        serializer = TaskDocumentSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass