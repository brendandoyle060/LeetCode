

class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0

        while i < len(nums):
            x = i + 1

            while x < len(nums):
                if nums[i] + nums[x] == target:
                    return [i, x]
                x += 1

            i += 1
