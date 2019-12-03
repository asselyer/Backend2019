from django.db import models
from users.models import MainUser

from api.constants import TASK_STATUSES, TASK_TODO, TASK_DONE, TASK_PRIORITIES, TASK_PRIORITY_MEDIUM, BLOCK_TYPES, BLOCK_TODO, BLOCK_IN_PROGRESS
from utils.upload import task_document_path
from utils.validators import validate_extension, validate_file_size

class Project(models.Model):

    name = models.CharField(max_length=300)
    desc = models.TextField(max_length=500)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    @property
    def tasks_count(self):
        return self.tasks.count()

class ProjectMember(models.Model):
    proj_user = models.ForeignKey(MainUser, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True, related_name='project_members', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.proj_user.username)


class BlockDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(types=BLOCK_TODO)

    def done_tasks(self):
        return self.filter(types=BLOCK_TODO)

    def filter_by_block_type(self, types):
        return self.filter(types=block_type)


class BlockInProgressManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(types=BLOCK_IN_PROGRESS)

    def done_tasks(self):
        return self.filter(types=BLOCK_IN_PROGRESS)

    def filter_by_block_type(self, types):
        return self.filter(types=block_type)


class Block(models.Model):
    name = models.CharField(max_length=255)
    types = models.PositiveIntegerField(choices=BLOCK_TYPES, default=BLOCK_TODO)
    projects = models.ForeignKey(Project, null=True,related_name='blocks', on_delete=models.CASCADE)
    done_blocks = BlockDoneManager()
    in_progress_tasks = BlockInProgressManager()
    objects = models.Manager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.types, self.projects)
    
    


class TaskDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_DONE)

    def done_tasks(self):
        return self.filter(status=TASK_DONE)

    def filter_by_status(self, status):
        return self.filter(status=status)


class TaskTodoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TASK_TODO)

    def done_tasks(self):
        return self.filter(status=TASK_DONE)

    def filter_by_status(self, status):
        return self.filter(status=status)

class BaseTask(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return '{}: {}'.format(self.id,self.name)

class Task(BaseTask):
    status = models.PositiveSmallIntegerField(choices=TASK_STATUSES, default=TASK_TODO)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='tasks', null=True)
    is_deleted = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(choices=TASK_PRIORITIES, default=TASK_PRIORITY_MEDIUM)
    executor = models.ForeignKey(MainUser, on_delete=models.SET_NULL, related_name='my_tasks', null=True)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_tasks')
    blocks = models.ForeignKey(Block,null=True, related_name='tasks', on_delete=models.CASCADE)
    objects = models.Manager()
    done_tasks = TaskDoneManager()
    todo_tasks = TaskTodoManager()

    class Meta:
        ordering = ('name', 'status',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'my_tasks'

    def __str__(self):
        return self.name

    def set_executor(self, executor_id):
        self.executor_id = executor_id
        self.save()
        
class TaskDocument(models.Model):
    document = models.FileField(upload_to=task_document_path, validators=[validate_file_size, validate_extension], blank=True, null=True)
    tasks = models.ForeignKey(Task, null=True, related_name='task_documents', on_delete=models.CASCADE)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id,self.document)

class TaskComment(models.Model):
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    tasks = models.ForeignKey(Task, null=True,  related_name='task_comments', on_delete=models.CASCADE)
   
    def __str__(self):
        return '{}: {}'.format(self.id, self.body, self.created_at)
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.body,
            'created_at': self.created_at
        }

