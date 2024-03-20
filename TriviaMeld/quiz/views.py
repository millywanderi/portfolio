from django.shortcuts import render
from .models import Quiz

# Create your views here.
def quiz_selection(request):
    """View to select a quiz"""
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_selection.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    """Provides deatails about the quiz"""
    quiz = Quiz.objects.get(pk=quiz_id)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})
