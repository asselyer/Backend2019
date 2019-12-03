from rest_framework import generics
from rest_framework import mixins

from api.models import Project, ProjectMember, TaskDocument, TaskComment
from api.serializers import ProjectSerializer, ProjectMemberSerializer, DashBoardSerializer, TaskDocumentSerializer, TaskCommentSerializer


class ProjectMemberView(generics.ListCreateAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer

class TaskDocumentCreateView(generics.CreateAPIView):
    queryset = TaskDocument.objects.all()
    serializer_class = TaskDocumentSerializer

class DashBoardView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = DashBoardSerializer

class TaskCommentCreateView(generics.CreateAPIView):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
