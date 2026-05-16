class Solution(object):
    def rob(self, nums):
        prev1 = 0
        prev2 = 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp
        return prev1