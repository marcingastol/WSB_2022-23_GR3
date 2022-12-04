import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

    def notest(self):
        pass

class MyTestCase2(unittest.TestCase):
    def test_two(self):
        pass

    def test_a(self):
        pass

if __name__ == "__main__":
    unittest.main()