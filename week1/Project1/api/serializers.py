from rest_framework import serializers
from api.models import Project, Task, TaskComment, TaskDocument
import json

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    class Meta:
        model = Task
        fields = ('id', 'name',)

class ProjectSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    tasks = TaskSerializer(many=True, read_only=True, required=False)

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    tasks = TaskSerializer(many=True, read_only=True, required=False)

class TaskDocumentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    document = serializers.FileField(required=False)

    class Meta:
        model = TaskDocument
        fields = ('id', 'document')

class TaskDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDocument
        fields = ['document']

class TaskCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    body = serializers.CharField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = TaskComment
        fields = '__all__'
        
class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    task_documents = TaskDocumentSerializer(many=True, read_only=True, required=False)
    task_comments = TaskCommentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = TaskDocument
        fields = ('id', 'name', 'description', 'task_documents', 'task_comments')

class BlockSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    block_type = serializers.CharField()
    projects = ProjectSerializer(many=True, read_only=True, required=False)