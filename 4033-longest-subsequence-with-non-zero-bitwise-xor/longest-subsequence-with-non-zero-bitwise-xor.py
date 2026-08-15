class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)
        x = 0

        for num in nums:
            x ^= num

        if x != 0:
            return n

        for num in nums:
            if num != 0:
                return n - 1

        return 0