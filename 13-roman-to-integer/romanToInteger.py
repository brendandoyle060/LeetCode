

class Solution:

    romans_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def convert(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.romans_dict[s]

    def nextCharIsLarger(self, s0, s1):
        """
        :type s0: str
        :type s1: str
        :rtype: bool
        """
        return self.convert(s0) < self.convert(s1)

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        length = len(s)
        i = 0
        for i in range(length):
            c = s[i]
            if i < length - 1:
                if self.nextCharIsLarger(c, s[i + 1]):
                    count -= self.convert(c)
                    continue
            count += self.convert(c)
        return count
