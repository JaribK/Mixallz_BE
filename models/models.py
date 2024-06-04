from django.db import models

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
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name