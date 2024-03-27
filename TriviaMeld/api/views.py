from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer
from quiz.models import Quiz, Question, Option

# Create your views here.

# Quiz API
@api_view(['GET'])
def quiz_list(request):
    """Displays the quizzes lists"""
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def post_quiz(request):
    """Adds quiz using post method"""
    if request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def quiz_detail(request, quiz_id):
    """Displays the quiz details"""
    try:
        quiz = Quiz.objects.get(quiz_id=quiz_id)
    except Quiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Question API
@api_view(['GET'])
def question_list(request):
    """Displays the questions lists"""
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def post_question(request):
    """Adds question using post method"""
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, question_id):
    """Displays the question details"""
    try:
        question = Question.objects.get(question_id=question_id)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Option API
@api_view(['GET'])
def option_list(request):
    """Displays the option lists"""
    if request.method == 'GET':
        options = Option.objects.all()
        serializer = OptionSerializer(options, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def post_option(request):
    """Adds an option using post method"""
    if request.method == 'POST':
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def option_detail(request, question_id):
    """Displays the option details"""
    try:
        option = Option.objects.get(question_id=question_id)
    except Option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OptionSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    