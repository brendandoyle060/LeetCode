

class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        strs = strs[1:]

        if len(strs) < 1:
            return prefix

        for i in range(len(prefix)):
            for s in strs:
                if i >= len(s):
                    return prefix[:i]
                if prefix[i] != s[i]:
                    return prefix[:i]

        return prefix
