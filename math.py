import unittest

class SimpleMath:
    def addition(a, b):
        return a+b

class TestSimpleMath(unittest.TestCase):
    def testadd(self):
        res = SimpleMath.addition(3, 2)
        self.assertEqual(res, 5)

if __name__ == "__main__":
    unittest.main()