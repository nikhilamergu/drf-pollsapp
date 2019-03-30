from django.test import TestCase


# Create your tests here.
class QuestionTest(TestCase):

    def test_question(self):

        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, 200)
