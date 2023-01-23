import unittest

from climbingStairs import Solution


class MyTestCase(unittest.TestCase):

    def test0(self):
        self.assertEqual(Solution().climbStairs(1), 1)

    def test1(self):
        self.assertEqual(Solution().climbStairs(2), 2)

    def test2(self):
        self.assertEqual(Solution().climbStairs(3), 3)

    def test3(self):
        self.assertEqual(Solution().climbStairs(4), 5)

    def test4(self):
        self.assertEqual(Solution().climbStairs(5), 8)

    def test5(self):
        self.assertEqual(Solution().climbStairs(38), 63245986)


if __name__ == '__main__':
    unittest.main()
