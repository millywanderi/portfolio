from django.db import models
from uuid import uuid4

# Create your models here.
def generate_id():
    """"Generates quiz id"""
    random_uuid = uuid4()
    quiz_id = f"{random_uuid}"
    return quiz_id

class Quiz(models.Model):
    """Model for quiz selection"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    quiz_id = models.CharField(max_length=10, default=generate_id, editable=False)


    class Meta:
        ordering = [
            'title' 
        ]

    def __str__(self):
        return f"({self.pk}) quiz {self.title}"
    

    