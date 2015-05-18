from django.test import TestCase


class HomeTestCase(TestCase):

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print('This should have raised an ERROR, but passed')
