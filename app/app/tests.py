"""
Sample Tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc Module"""
    def test_add(self):
        """Test the adding of two numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub(self):
        """Test the subtraction of two numbers"""
        res = calc.sub(5, 6)
        self.assertEqual(res, 1)
