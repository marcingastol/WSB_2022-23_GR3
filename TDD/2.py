import unittest

class Dodawanie(unittest.TestCase):
    def test_main(self):
        result = addition(3,6,2)
        assert result == 11


def addition(*args):
    total = 0
    for i in args:
        total += i
    return total

if __name__ == "__main__":
    unittest.main()