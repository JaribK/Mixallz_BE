import uuid
from django.db import models
from users.models import Users
from datetime import datetime

# Create your models here.
class ListFeatures(models.Model):
    status = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('in_progress', 'In Progress'),
        ('in_development', 'In Development')
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=status, default='active')
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Code(models.Model):
    code = models.CharField(max_length=50,null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class UserCodeRedemption(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'code')