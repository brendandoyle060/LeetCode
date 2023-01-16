import unittest

from romanToInteger import Solution


class MyTestCase(unittest.TestCase):

    def test_52(self):
        self.assertEqual(Solution().romanToInt("LII"), 52)

    def test_3(self):
        self.assertEqual(Solution().romanToInt("III"), 3)

    def test_58(self):
        self.assertEqual(Solution().romanToInt("LVIII"), 58)

    def test_1994(self):
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)

    def test_min_val(self):
        self.assertEqual(Solution().romanToInt("I"), 1)

    def test_max_val(self):
        self.assertEqual(Solution().romanToInt("MMMCMXCIX"), 3999)

    def test_max_length(self):
        self.assertEqual(Solution().romanToInt("MMMDCCCLXXXVIII"), 3888)

    def test_all_singles(self):
        self.assertEqual(Solution().romanToInt("MDCLXVI"), 1666)

    # Probably not actually a valid Roman Numeral, but a convenient way to test
    # all different doubles at once.
    def test_all_doubles(self):
        self.assertEqual(Solution().romanToInt("CMCDXCXLIXIV"), 1443)


if __name__ == '__main__':
    unittest.main()
