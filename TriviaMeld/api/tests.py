from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from Quiz.models import Quiz, Question, Option
from .serializers import QuizSerializer
from .views import question_list, post_question, question_detail

# Test for QuizAPI.
class QuizAPITests(TestCase):
    """Test for Quiz API"""
    def setUp(self):
        """Set up the quiz"""
        self.client = APIClient()
        self.quiz_data = {
            'title': 'Quiz 1',
            'image': 'quiz_image.jpg',
            'description': 'Test your knowledge of maths'
        }
        self.quiz = Quiz.objects.create(**self.quiz_data)


    def test_get_quiz_list(self):
        """Test for quiz_list api"""
        reponse = self.client.get(reverse('quiz_list'))
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_quiz(self):
        """Test for creating a quiz using API"""
        response = self.client.post(reverse('post_quiz'), self.quiz_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_quiz_detail(self):
        """Get the quiz details using get method"""
        response = self.client.get(reverse('quiz_detail', kwargs={'quiz_id': self.quiz.id}))
        serializer = QuizSerializer(self.quiz)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_put_quiz_detail(self):
        """Edit the quiz detail"""
        updated_data = {
            'title': 'Updated Quiz 1',
            'image': 'updated_image.jpg',
            'description': 'Test your knowledge of simple maths - updated description'
        }
        response = self.client.put(reverse('quiz_detail', kwargs={'quiz_id': self.quiz.id}), updated_data, format='json')
        updated_quiz = Quiz.objects.get(id=self.quiz.id)
        serializer = QuizSerializer(updated_quiz)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_delete_quiz_detail(self):
        """Test to delete quiz detail"""
        response = self.client.delete(reverse('quiz_detail', kwargs={'quiz_id', self.quiz.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 


# Test for Question API. 
class QuestionAPITests(TestCase):
    """Test for Question API""" 
    def setUp(self):
        """Set up the question"""
        self.factory = APIRequestFactory()
        self.question_data = {'text': 'Test question test'}


    def test_question_list(self):
        """Test for question API list"""
        request = self.factory.get('/questions/')
        response = question_list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_question(self):
        """Test for creating question API"""
        request = self.factory.post('/questions/', self.question_data)
        response = post_question(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_question_detail_get(self):
        """Get the question API test"""
        question = Question.objects.create(text='Test question')
        request = self.factory.get(f'/questions/{question.id}/')
        response = question_detail(request, question_id=question.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_question_detail_put(self):
        """Test for updating question api detail"""
        question = Question.objects.create(text='Text question')
        updated_data = {'text': 'Updated test question test'}
        request = self.factory.put(f'/questions/{question.id}/', updated_data)
        response = question_detail(request, question_id=question.id)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], updated_data['text'])


    def test_question_detail_delete(self):
        """Test for deleting the question api detail"""
        question = Question.objects.create(text='Test question')
        request = self.factory.delete(f'/questions/{question.id}/')
        response = question_detail(request, question_id=question.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Test for Option API. 
class OptionAPITests(TestCase):
    """Test for Option API"""
    def setUp(self):
        """Set up the options"""
        self.client = APIClient()
        self.option_data = {'question_id': 1, 'test': 'Option A'}


    def test_option_list(self):
        """Test for display option api list"""
        response = self.client.get(reverse('option_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_option(self):
        """Test for creating an option api"""
        response = self.client.post(reverse('post_option'), self.option_data, format='json')
        self.asserEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Option.objects.count(), 1)


    def test_option_detail_get(self):
        """Test for option api get details"""
        option =Option.objects.create(question_id=1, text='Option A')
        response = self.client.get(reverse('option_detail', kwargs={'question_id': option.question_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_option_detail_put(self):
       """Test for updating option detail api"""
       option = Option.objects.create(question_id, text='Option A')
       updated_data = {'question_id': 1, 'text': 'Option A'}
       response = self.client.put(reverse('option_detail', kwargs={'question_id': option.question_id}), updated_data, format='json')
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       option.refresh_from_db()
       self.assertEqual(option.text, 'Option B') 
    

    def test_option_detail_delete(self):
        """Test for deleting option api detail"""
        option = Option.objects.create(question_id=1, text='Option A')
        response = self.client.delete(reverse('option_detail', kwargs={'question_id': option.question_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Option.objects.count(), 0)
