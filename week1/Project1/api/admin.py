from django.contrib import admin
from api.models import Task, Project, Block, TaskComment, TaskDocument

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Block)
admin.site.register(TaskDocument)
admin.site.register(TaskComment)

