from api.models import Project, Task, ProjectMember, TaskComment, TaskDocument, Block
from rest_framework import serializers

from users.serializers import UserSerializer


class BlockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Block
        fields = '__all__'

class ProjectMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectMember
        fields = ('id', 'proj_user', 'project')

class ProjectSerializer2(serializers.ModelSerializer):

    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    desc = serializers.CharField(required=False)

    class Meta:
        model = Project
        fields = ('id', 'name','creator', 'desc' )

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tasks_count = serializers.IntegerField(default=0, read_only=True)
    desc = serializers.CharField(required=False)

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return obj.creator.username == 'Anonymus'

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        return project
    

class TaskDocumentSerializer(serializers.ModelSerializer):
    document = serializers.FileField(required=False)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaskDocument
        fields = ('id', 'document', 'creator', 'tasks')

class TaskDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDocument
        fields = ['document']

class TaskCommentSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaskComment
        fields = ('id', 'body', 'creator', 'created_at','tasks')

class TaskSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    status = serializers.IntegerField()
    description = serializers.CharField()
    priority = serializers.IntegerField()
    is_deleted = serializers.BooleanField(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.description = validated_data.get('description', instance.description)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.project_id = validated_data.get('project_id', instance.project_id)

        instance.save()
        return instance

    def validate_status(self, value):
        if 1 < value > 3:
            raise serializers.ValidationError('status options: [1, 2, 3]')
        return value

class TaskShortSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True)
    creator = UserSerializer(read_only=True)
    executor = UserSerializer(read_only=True)

    #document = serializers.FileField(write_only=True)
    #document_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status', 'project_id', 'executor','creator')

    # def get_document_url(self, obj):
    #     if obj.document:
    #         return self.context['request'].build_absolute_uri(obj.document.url)
    #     return None

class SetExecutorSerializer(serializers.ModelSerializer):
    executor = UserSerializer()
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # document = serializers.FileField(write_only=True)
    # document_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Task
        fields = ('creator', 'executor')



class TaskFullSerializer(TaskShortSerializer):
    task_documents = TaskDocumentSerializer(many=True, read_only=True, required=False)
    task_comments = TaskCommentSerializer(many=True, read_only=True, required=False)

    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description', 'task_documents', 'task_comments')

class TaskChangeSerializer(serializers.ModelSerializer):
    # task_comments = TaskCommentSerializer(many=True, read_only=True, required=False)
    task_documents = TaskDocumentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Task
        fields = ('id', 'name', 'task_documents', 'status', 'project', 'executor', 'creator')





class DashBoardSerializer(ProjectSerializer2):
    pass