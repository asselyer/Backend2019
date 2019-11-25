from rest_framework import serializers
from api.models import MainUser, Profile, Block, Project, Task, TaskComment, TaskDocument, ProjectMember


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = MainUser.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    web_site = serializers.CharField()
    # avatar = serializers.ImageField()

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'web_site','avatar')
        read_only_fields = ('username',)

    def get_avatar_url(self, obj):
        return obj.avatar.url

class ProfileSerializer1(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    bio = serializers.CharField(allow_blank=True, required=False)
    web_site = serializers.CharField()
    # avatar = serializers.ImageField()

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'web_site','avatar')
        read_only_fields = ('username',)

    def get_avatar_url(self, obj):
        return obj.avatar.url

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    class Meta:
        model = Task
        fields = ('id', 'name',)

class ProjectMemberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(source='user.username')

    class Meta:
        model = ProjectMember
        fields = ('id', 'user')

class ProjectSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    creator = serializers.CharField(source='creator.username')
    description = serializers.CharField()
    tasks = TaskSerializer(many=True, read_only=True, required=False)
    project_members = ProjectMemberSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Project
        fields = ('id', 'name','creator', 'description', 'tasks', 'project_members')

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    tasks = TaskSerializer(many=True, read_only=True, required=False)
    creator = serializers.CharField(source='creator.username')
    tasks_count = serializers.IntegerField(default=0, read_only=True)

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
    creator = serializers.CharField(source='creator.username')

    class Meta:
        model = TaskComment
        fields = '__all__'
        
class TaskSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    creator = serializers.CharField(source='creator.username')
    description = serializers.CharField()
    task_documents = TaskDocumentSerializer(many=True, read_only=True, required=False)
    task_comments = TaskCommentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = TaskDocument
        fields = ('id', 'name', 'description', 'creator', 'task_documents', 'task_comments')

class ProjectSerializer3(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    creator = serializers.CharField(source='creator.username')
    description = serializers.CharField()
    tasks = TaskSerializer2(many=True, read_only=True, required=False)
    project_members = ProjectMemberSerializer(many=True, read_only=True, required=False)
    blocks = BlockSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Project
        fields = ('id', 'name','creator', 'description', 'tasks', 'project_members')

class BlockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    block_type = serializers.CharField()
    projects = ProjectSerializer(many=True, read_only=True, required=False)

    class Meta:
            model = Block
            fields = '__all__'