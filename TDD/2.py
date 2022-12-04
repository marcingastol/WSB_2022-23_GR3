import unittest

class Dodawanie(unittest.TestCase):
    def test_main(self):
        result = addition(3,6)
        assert result == 10


def addition(arg1, arg2):
    return arg1 + arg2

if __name__ == "__main__":
    unittest.main()