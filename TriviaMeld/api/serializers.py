from rest_framework import serializers
from quiz.models import Quiz, Question, Option
# Create your models here.

class QuizSerializer(serializers.ModelSerializer):
    """Create Quiz API model"""
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    """Create Question API model"""
    class Meta:
        model = Question
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    """Create Option API model"""
    class Meta:
        model = Option
        fields = '__all__'