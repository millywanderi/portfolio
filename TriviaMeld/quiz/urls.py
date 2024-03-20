from django.urls import path
from . import views

urlpatterns = [
    path('quiz-selection', views.quiz_selection, name='quiz_selection'),
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]
