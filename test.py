from whiteboard import solution
from unittest import TestCase


class TestWhiteboard(TestCase):

    def test_empty_arr(self):
        self.assertEqual(solution([]), -1)

    def test_single_lucky_number(self):
        self.assertEqual(solution([2, 2, 3]), 2)

    def test_multiple_lucky_numbers(self):
        self.assertEqual(solution([1, 2, 2, 3, 3, 3]), 3)




