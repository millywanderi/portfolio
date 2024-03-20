from django.db import models

# Create your models here.
class Quiz(models.Model):
    """Model for quiz selection"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    