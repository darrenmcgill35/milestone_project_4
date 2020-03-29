from django.test import TestCase
from .models import Store

# Create your tests here.
class StoreTests(TestCase):

    def test_str(self):
        test_name = Store(name='Football')
        self.assertEqual(str(test_name), 'Football')


