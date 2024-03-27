from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/add', views.post_quiz, name='post_quiz'),
    path('quizzes/<int:quiz_id>', views.quiz_detail, name='quiz_detail'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/add', views.post_question, name='post_question'),
    path('questions/<int:question_id>', views.question_detail, name='question_detail'),
    path('options/', views.option_list, name='option_list'),
    path('options/add', views.post_option, name='post_option'),
    path('options/<int:question_id>', views.option_detail, name='option_detail'),
]