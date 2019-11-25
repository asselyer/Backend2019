from django.db import models
from datetime import date
from django.utils import timezone

class Block(models.Model):
    name = models.CharField(max_length=255)
    block_type = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.block_type, self.projects)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    blocks = models.ForeignKey(Block, null=True,related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.description, self.tasks)

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    projects = models.ForeignKey(Project, null=True, related_name='tasks', on_delete=models.CASCADE)
    # task_comments = models.ForeignKey(TaskComment, related_name='TaskComment', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.description)

class TaskDocument(models.Model):
    document = models.FileField(upload_to='task_documents', blank=True, null=True)
    tasks = models.ForeignKey(Task, null=True, related_name='task_documents', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id,self.document)

class TaskComment(models.Model):
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
