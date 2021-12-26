import unittest

from my_crawler.my_calculator import custom_add
from my_crawler.my_calculator import custom_minus
from my_crawler.my_calculator import custom_multiply
from my_crawler.my_calculator import custom_divide


class CustomTests (unittest.TestCase) :
    def test_custom_add(self):
        self.assertEqual(129, custom_add(109,20))
    def test_custom_minus(self):
        self.assertEqual(89, custom_minus(109,20))
    def test_custom_multiply(self):
        self.assertEqual(2180, custom_multiply(109,20))
    def test_custom_divide(self):
        self.assertAlmostEqual(5.45, custom_divide(109,20))

# unittest 실행
if __name__ == '__main__':
    unittest.main()