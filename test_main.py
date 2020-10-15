import unittest
from main import puzzle_solver


class PuZZle(unittest.TestCase):
    def test_simple_puzzle(self):

        simple_puzzle = [((None, 5), (None, None), 3),
                         ((17, None), (None, None), 9),
                         ((None, 4), (None, 5), 8),
                         ((4, 11), (5, 17), 5),
                         ((11, None), (17, None), 2),
                         ((None, None), (None, 4), 7),
                         ((5, 17), (None, None), 1),
                         ((None, None), (11, None), 4),
                         ((None, None), (4, 11), 6)]

        simple_puzzle_answer = [(7, 6, 4), (8, 5, 2), (3, 1, 9)]

        res = puzzle_solver(simple_puzzle, 3, 3)
        self.assertEqual(res, simple_puzzle_answer)


if __name__ == '__main__':
    unittest.main()
