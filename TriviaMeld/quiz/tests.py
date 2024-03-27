from django.test import TestCase
from django.urls import reverse
from .models import Quiz, Question, Option

# Create your tests here.

class QuizViewTests(TestCase):
    """Test for quiz view"""
    def setUp(self):
        """Set up the class"""
        self.quiz = Quiz.objects.create(title='Test Quiz')
        self.question1 = Question.objects.create(quiz=self.quiz, text='Question 1')
        self.question2 = Question.objects.create(quiz=self.quiz, text='Question 2')
        self.question1 = Question.objects.create(quiz=self.quiz, text='Question 3')
        self.option1_1 = Option.objects.create(question=self.question1, text='Option 1 for Question 1', is_correct=True)
        self.option1_2 = Option.objects.create(question=self.question1, text='Option 2 for Question 1', is_correct=False)
        self.option2_1 = Option.objects.create(question=self.question2, text='Option 1 for Question 2', is_correct=True)
        self.option2_2 = Option.objects.create(question=self.question1, text='Option 2 for Question 2', is_correct=False)
        self.option3_1 = Option.objects.create(question=self.question1, text='Option 1 for Question 3', is_correct=True)
        self.option3_2 = Option.objects.create(question=self.question1, text='Option 2 for Question 3', is_correct=False)


    def test_quiz_selection(self):
        """Test for quiz selection"""
        response = self.client.get(reverse('quiz:quiz_selection'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerrysetEqual(response.context['quizzes'], [repr(self.quiz)])
        

    def test_quiz_interface(self):
        """Test for quiz interface"""
        response = self.client.get(reverse('quiz:quiz_interface', args: self.quiz.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['quiz'], self.quiz)
        self.assertQuerrysetEqual(response, context['questions'], [repr(self.question1), repr(self.question2), repr(self.question3)])

    
    def test_submit_correct_answer(self):
        """Test for submitting the correct answer"""
        response = self.client.post(reverse('quiz:submit_answer', args=self.quiz.id)), {'Question 1': self.option1_1.text, 'Question 2': self.option2_1.text, 'Question 3': self.option3_1.text}
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '3/3')


    def test_submit_incorrect_answer(self):
        """Test for submitting the correct answer"""
        response = self.client.post(reverse('quiz:submit_answer', args=self.quiz.id)), {'Question 1': self.option1_2.text, 'Question 2': self.option2_2.text, 'Question 3': self.option3_2.text}
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '0/3')
