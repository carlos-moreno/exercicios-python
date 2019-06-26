import unittest

from havelhakimi import warmup1, warmup2, warmup3, warmup4, hh


class HavelhakimiTest(unittest.TestCase):
    def test_eliminating_0(self):
        lists_of_test = (
            [5, 3, 0, 2, 6, 2, 0, 7, 2, 5],
            [4, 0, 0, 1, 3],
            [1, 2, 3],
            [0, 0, 0],
            []
        )
        lists_of_comparable = (
            [5, 3, 2, 6, 2, 7, 2, 5],
            [4, 1, 3],
            [1, 2, 3],
            [],
            []
        )
        for x, y in zip(lists_of_test, lists_of_comparable):
            with self.subTest():
                self.assertEqual(warmup1(x), y)

    def test_descending_sort(self):
        lists_of_test = (
            [5, 1, 3, 4, 2],
            [0, 0, 0, 4, 0],
            [1],
            []
        )
        list_of_comparable = (
            [5, 4, 3, 2, 1],
            [4, 0, 0, 0, 0],
            [1],
            []
        )
        for x, y in zip(lists_of_test, list_of_comparable):
            with self.subTest():
                self.assertEqual(warmup2(x), y)

    def test_length_check(self):
        self.assertFalse(warmup3(7, [6, 5, 5, 3, 2, 2, 2]))
        self.assertFalse(warmup3(5, [5, 5, 5, 5, 5]))
        self.assertFalse(warmup3(0, []))
        self.assertTrue(warmup3(5, [5, 5, 5, 5]))
        self.assertTrue(warmup3(3, [1, 1]))
        self.assertTrue(warmup3(1, []))

    def test_front_elimination(self):
        self.assertEqual(warmup4(4, [5, 4, 3, 2, 1]), [4, 3, 2, 1, 1])
        self.assertEqual(warmup4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]),
                         [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2])
        self.assertEqual(warmup4(1, [10, 10, 10]), [9, 10, 10])
        self.assertEqual(warmup4(3, [10, 10, 10]), [9, 9, 9])
        self.assertEqual(warmup4(1, [1]), [0])

    def test_hh(self):
        self.assertEqual(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]), False)
        self.assertEqual(hh([4, 2, 0, 1, 5, 0]), False)
        self.assertEqual(hh([3, 1, 2, 3, 1, 0]), True)
        self.assertEqual(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]), True)
        self.assertEqual(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]), True)
        self.assertEqual(hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]), False)
        self.assertEqual(hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]), False)
        self.assertEqual(hh([2, 2, 0]), False)
        self.assertEqual(hh([3, 2, 1]), False)
        self.assertEqual(hh([1, 1]), True)
        self.assertEqual(hh([1]), False)
        self.assertEqual(hh([]), True)
