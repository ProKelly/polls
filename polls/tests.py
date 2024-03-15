
import datetime
from django.test import TestCase
from django.utils import timezone 
from polls.models import Question
from django.urls import reverse

# class QuestionModelTestCase(TestCase):#all test classes must end with TestCase or Tests
#     def test_was_published_recently(self):#all test methods must begin with test_
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)
    
#     def test_was_published_recently_with_old_question(self):
#         time = timezone.now()-datetime.timedelta(days=1, seconds=1)
#         old_question = Question(pub_date=time)
#         self.assertIs(old_question.was_published_recently(), False)
    
#     def test_was_published_recently_with_recent_question(self):
#         time = timezone.now()-datetime.timedelta(hours=23, minutes=59, seconds=59)
#         recent_question = Question(pub_date=time)
#         self.assertIs(recent_question.was_published_recently(), True)
    

def create_question(question_text, days):
    time = timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")

        self.assertQuerySetEqual(response.context['lastest_question_list'], [])

    def test_past_questions(self):
        question = create_question(question_text="past question", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            [question],
        )
    
    def test_future_questions(self):
        create_question(question_text="Future Question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")

        self.assertQuerySetEqual(
            response.context['latest_question_list'] , []
        )
    
    def test_future_questions_and_past_questions(self):
        question = create_question(question_text="past questions", days=-30)
        create_question(question_text="Future question", days=30)
        