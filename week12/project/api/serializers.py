from api.models import Project, Task
from rest_framework import serializers

from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()
    # my_name = serializers.SerializerMethodField()
    # creator_name = serializers.SerializerMethodField()
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tasks_count = serializers.IntegerField(default=0, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'desc', 'creator', 'tasks_count')

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return obj.creator.username

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
        fields = ('id', 'name', 'document', 'status', 'project_id', 'executor','creator')

    # def get_document_url(self, obj):
    #     if obj.document:
    #         return self.context['request'].build_absolute_uri(obj.document.url)
    #     return None

# class SetExecutorSerializer(serializers.ModelSerializer):
#     executor = UserSerializer()
#     creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     # document = serializers.FileField(write_only=True)
#     # document_url = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Task
#         fields = ('creator', 'executor')



class TaskFullSerializer(TaskShortSerializer):
    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description')

class TaskChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'document', 'status', 'project', 'executor', 'creator')




