from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser, User


class MainUser(AbstractUser):
    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'

        def __str__(self):
            return f'{self.id}: {self.username}'

class UserProfile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.username}'

class ProductServiceBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Product(ProductServiceBase):
    TYPE_TECH = 1
    TYPE_HOME = 2
    TYPE_CLOTH = 3
    PROD_TYPES = (
        (TYPE_TECH, 'Technology'),
        (TYPE_HOME, 'Home'),
        (TYPE_CLOTH, 'Clothes'),
                )                    
    size = models.IntegerField()
    product_type = models.PositiveSmallIntegerField(choices=PROD_TYPES, default=TYPE_TECH)
    existence = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Service(ProductServiceBase):
    S_SAFE = 1
    S_CHECKED = 2
    SERVICE_TYPES = (
        (S_SAFE, 'Safe'),
        (S_CHECKED, 'Checked'),

                )   
    approximate_duration = models.IntegerField()
    service_type = models.PositiveSmallIntegerField(choices=SERVICE_TYPES, default=S_SAFE)

    def __str__(self):
        return f'{self.id}: {self.name}'