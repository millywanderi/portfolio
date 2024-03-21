from django.shortcuts import render, get_object_or_404
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

def quiz_interface(request, quiz_id):
    """Retrieve the quiz object from the database based on quiz_id"""
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    # questions = quiz.question_set.all()
    return render(request, 'quiz/quiz_interface.html', {'quiz': quiz})
