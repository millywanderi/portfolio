from django.db import models
from uuid import uuid4

# Create your models here.
def generate_id():
    """"Generates quiz id"""
    random_uuid = uuid4()
    return str(random_uuid)[:8]

class Quiz(models.Model):
    """Model for quiz selection"""
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='quiz', blank=True, null=True)
    description = models.TextField()
    quiz_id = models.CharField(max_length=10, default=generate_id, editable=False)


    class Meta:
        ordering = [
            'title' 
        ]

    def __str__(self):
        return f"({self.pk}) quiz {self.title}"
    

class Question(models.Model):
    """Model for quiz questions"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_name = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        """Str method"""
        return f"{self.pk} Question: {self.text}"
    
    @property
    def question_choices(self):
        choices = Option.objects.filter(question=self)
        return choices
    

class Option(models.Model):
    """Model for question options"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    related_options = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        """Str method"""
        return f"Option: {self.text} (Correct: {self.is_correct})"
    