"""Module for testing the Github Actions workflow"""

import unittest

class SimpleMath:
    """class for storing simple math functions"""
    def addition(self, a, b):
        """Addition function, return the sum of its two arguments a and b."""
        return a+b

    def subtraction(self, a, b):
        """Subtraction function, return the difference of its two arguments a and b."""
        return a-b

class TestSimpleMath(unittest.TestCase):
    """UT class for SimpleMath"""
    def testadd(self):
        """testing function for SimpleMath.addition"""
        res = SimpleMath.addition(self, 3, 2)
        self.assertEqual(res, 5)

    def testsub(self):
        """testing function for SimpleMath.subtraction"""
        res = SimpleMath.subtraction(self, 3, 2)
        self.assertEqual(res, 1)

if __name__ == "__main__":
    unittest.main()
