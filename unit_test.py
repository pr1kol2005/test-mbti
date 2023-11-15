import unittest
from main import arithmetical_mean


class TestFunc(unittest.TestCase):
    def test_square(self):
        self.assertEqual(arithmetical_mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(arithmetical_mean([1, 1, 1]), 1)
        self.assertEqual(arithmetical_mean([2, 3, 4, 5]), 3.5)


if __name__ == '__main__':
    unittest.main()
