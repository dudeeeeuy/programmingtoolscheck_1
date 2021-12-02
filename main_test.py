import unittest
from main import print_hi_stephen, print_hi_matthew, print_hi_rick_astley


class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen(), f"Hi, Stephen")

    def test_print_hi_matthew(self):
        self.assertEqual(print_hi_matthew(), f"Hi, Matthew")

    def test_print_hi_rick_astley(self):
        self.assertEqual(print_hi_rick_astley(), f"Hi, Rick_Astley")


if __name__ == '__main__':
    unittest.main()
