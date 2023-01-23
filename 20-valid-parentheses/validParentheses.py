from collections import deque

openParen = {
    "(": ")",
    "[": "]",
    "{": "}"
}


class Solution:

    def isOpenParen(self, c):
        """
        :type c: str
        :rtype: bool
        """
        return c in openParen.keys()

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Length of list must be even in order to have matching parens
        if len(s) % 2 != 0:
            return False

        stack = deque()

        i = 0
        while i < len(s):
            c = s[i]
            if self.isOpenParen(c):
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False

                if openParen[stack.pop()] != c:
                    return False

            i += 1

        return len(stack) == 0
