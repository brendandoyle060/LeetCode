

class Solution:

    solved = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        if self.solved.get(n):
            return self.solved[n]
        else:
            x = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.solved[n] = x
            return x
        