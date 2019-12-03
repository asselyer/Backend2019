from django.contrib import admin
from api.models import ProjectMember, Task, Project, Block, TaskComment, TaskDocument


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'project', 'executor', 'creator')


admin.site.register(ProjectMember)
admin.site.register(Block)
admin.site.register(TaskComment)
admin.site.register(TaskDocument)