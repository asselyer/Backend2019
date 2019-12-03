from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token


class MainUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_login}'

    def __str__(self):
        return f'{self.id}: {self.username}'

