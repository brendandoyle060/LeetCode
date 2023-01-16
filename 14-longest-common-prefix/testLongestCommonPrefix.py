import unittest

from longestCommonPrefix import Solution


class MyTestCase(unittest.TestCase):

    def test0(self):
        self.assertEqual(Solution().longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test1(self):
        self.assertEqual(Solution().longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test2(self):
        self.assertEqual(Solution().longestCommonPrefix(["dog"]), "dog")

    def test3(self):
        self.assertEqual(Solution().longestCommonPrefix([""]), "")

    def test4(self):
        self.assertEqual(Solution().longestCommonPrefix(["dog", ""]), "")

    def test5(self):
        self.assertEqual(Solution().longestCommonPrefix(["ab", "a"]), "a")

    def test6(self):
        self.assertEqual(Solution().longestCommonPrefix(["a", "ab"]), "a")

    def test7(self):
        self.assertEqual(Solution().longestCommonPrefix(["str", "stri", "string"]), "str")

    def test8(self):
        self.assertEqual(Solution().longestCommonPrefix(["str", "stri", "string", "xcv"]), "")

    def test9(self):
        self.assertEqual(Solution().longestCommonPrefix(["str", "stri", "spf", "string"]), "s")


if __name__ == '__main__':
    unittest.main()
