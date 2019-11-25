from django.db import models
from datetime import date
from django.utils import timezone

from django.contrib.auth.models import User, AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


class MainUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    web_site = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='user_images', default='default.png', blank=True, null=True)

    def __str__(self):
        return f'{self.id}: {self.user.username}'

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=MainUser)

class Block(models.Model):
    name = models.CharField(max_length=255)
    block_type = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.block_type, self.projects)

class Project(models.Model):
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    blocks = models.ForeignKey(Block, null=True,related_name='projects', on_delete=models.CASCADE)
    # project_members = models.ForeignKey(ProjectMember, null=True, related_name='project_members', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.creator, self.description, self.tasks,self.project_members)

class ProjectMember(models.Model):
    user = models.ForeignKey(MainUser, null=True, on_delete=models.CASCADE)
    projects = models.ForeignKey(Project, null=True, related_name='project_members', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.user.username)

class Task(models.Model):
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    projects = models.ForeignKey(Project, null=True, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.creator,self.description)

class TaskDocument(models.Model):
    document = models.FileField(upload_to='task_documents', blank=True, null=True)
    tasks = models.ForeignKey(Task, null=True, related_name='task_documents', on_delete=models.CASCADE)

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
