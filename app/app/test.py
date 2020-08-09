from django.test import TestCase
from app.calc import add, subtract

class ClasTestCase(TestCase):
    
    def test_add_number(self):
        print("Test add is working")
        self.assertEqual(add(3,8), 11)
        
        
    def test_subtract_number(self):
        print("subtract given number")
        self.assertEqual(subtract(5, 11), 6)