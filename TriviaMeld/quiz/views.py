from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Option

# Create your views here.
def quiz_selection(request):
    """View to select a quiz"""
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_selection.html', {'quizzes': quizzes})


def quiz_interface(request, quiz_id):
    """Retrieve the quiz object from the database based on quiz_id"""
    quiz = get_object_or_404(Quiz, id=quiz_id)
    # questions = quiz.questions.all()
    questions = Question.objects.filter(quiz=quiz)
    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quiz/quiz_interface.html', context)


def submit_answer(request, quiz_id):
    """Submitting the answer"""
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        question1_answer = request.POST['Question 1']
        question2_answer = request.POST['Question 2']
        question3_answer = request.POST['Question 3']
        answers_list = [
            question1_answer,
            question2_answer,
            question3_answer
        ]

        questions = Question.objects.filter(quiz=quiz)
        score = 0
        total_score = 0

        for question in questions:
            correct_answer = Option.objects.get(question=question, is_correct=True)
            for answer in answers_list:
                print("correct_answer", correct_answer.text, type(correct_answer.text))
                print("user_answer", answer, type(answer))
                if correct_answer.text == answer:
                    score += 1           
        total_score = f"{score}/3"
        context = {
            'total_score': total_score,
        }
        return render(request, 'quiz/quiz_feedback.html', context)
