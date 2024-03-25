from django.urls import path
from . import views

urlpatterns = [
    path('quiz-selection', views.quiz_selection, name='quiz_selection'),
    #path('quiz-detail/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz-interface/<int:quiz_id>/', views.quiz_interface, name="quiz_interface"),
    #path('quiz-interface/<int:quiz_id>/question-details/<int:question_id>/', views.question_details, name='question_details'),
    #path('quiz/<int:quiz_id>/', views.quiz, name='quiz'),
    path('submit_answer/<int:quiz_id>', views.submit_answer, name='submit_answer'),
]
