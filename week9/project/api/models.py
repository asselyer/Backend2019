from django.db import models
from users.models import MainUser

from api.constants import TASK_STATUSES, TASK_TODO, TASK_DONE, TASK_PRIORITIES, TASK_PRIORITY_MEDIUM
from utils.upload import task_document_path
from utils.validators import validate_extension, validate_file_size

class Project(models.Model):

    name = models.CharField(max_length=300)
    desc = models.TextField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    @property
    def tasks_count(self):
        return self.tasks.count()


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


class Task(models.Model):
    document = models.FileField(upload_to=task_document_path, validators=[validate_file_size, validate_extension], blank=True, null=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=TASK_STATUSES, default=TASK_TODO)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='tasks', null=True)
    is_deleted = models.BooleanField(default=False)
    description = models.TextField(default='')
    priority = models.PositiveIntegerField(choices=TASK_PRIORITIES, default=TASK_PRIORITY_MEDIUM)
    executor = models.ForeignKey(MainUser, on_delete=models.SET_NULL, related_name='my_tasks', null=True)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_tasks')

    objects = models.Manager()
    done_tasks = TaskDoneManager()
    todo_tasks = TaskTodoManager()

    class Meta:
        unique_together = ('project', 'name')
        ordering = ('name', 'status',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'my_tasks'

    def __str__(self):
        return self.name

    def set_executor(self, executor_id):
        self.executor_id = executor_id
        self.save()
        



class BaseTask(models.Model):
    name = models.CharField(max_length=300)
    desc = models.TextField()

    def get_short_name(self):
        return self.name[:3]

    @property
    def short_name(self):
        return self.name[:3]

    def set_name(self, name):
        self.name = name
        self.save()

    def show_info(self):
        raise NotImplementedError(
            'must be implemented'
        )

    class Meta:
        ordering = ('-name',)
        abstract = True


class DeveloperTask(BaseTask):
    name = models.CharField(max_length=200)

    # tasks = models.Manager()

    class Meta(BaseTask.Meta):
        ordering = (BaseTask.Meta.ordering, 'desc')
        unique_together = ('name', 'desc')


class StaffTask(BaseTask):
    message = models.CharField(max_length=100)

    def show_info(self):
        return ''

