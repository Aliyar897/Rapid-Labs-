from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


class Team(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'manager'}
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='teams', 
        blank=True
    )

    def __str__(self):
        return self.name
