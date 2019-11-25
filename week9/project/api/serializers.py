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


class TaskShortSerializer(serializers.ModelSerializer):
    is_deleted = serializers.BooleanField(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    executor = UserSerializer(read_only=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ('id', 'name', 'document', 'status', 'is_deleted', 'project_id', 'executor', 'creator')


class TaskFullSerializer(TaskShortSerializer):
    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description',)

class TaskChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'document', 'status', 'project', 'executor', 'creator')




