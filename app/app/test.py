from django.test import TestCase
from app.calc import add

class ClasTestCase(TestCase):
    
    def test_add_number(self):
        print("Test add is working")
        self.assertEqual(add(3,8), 11)