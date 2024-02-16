import unittest

class SimpleMath:
    def addition(a, b):
        return a+b

class TestSimpleMath(unittest.TestCase):
    def testadd():
        res = addition(3, 2)
        self.assertEqual(res, 5)