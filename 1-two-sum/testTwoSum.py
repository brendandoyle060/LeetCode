import unittest

from twoSum import Solution


class MyTestCase(unittest.TestCase):

    def test0(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test1(self):
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])

    def test2(self):
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
