import unittest

from validParentheses import Solution


class MyTestCase(unittest.TestCase):

    def test0(self):
        self.assertEqual(Solution().isValid("()"), True)

    def test1(self):
        self.assertEqual(Solution().isValid("()[]{}"), True)

    def test2(self):
        self.assertEqual(Solution().isValid("(]"), False)

    def test3(self):
        self.assertEqual(Solution().isValid("{[()]}"), True)

    def test4(self):
        self.assertEqual(Solution().isValid("{[]()}"), True)

    def test5(self):
        self.assertEqual(Solution().isValid("("), False)

    def test6(self):
        self.assertEqual(Solution().isValid("{[]}"), True)


if __name__ == '__main__':
    unittest.main()
