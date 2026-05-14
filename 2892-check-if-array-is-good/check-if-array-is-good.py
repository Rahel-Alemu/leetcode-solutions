class Solution(object):
    def isGood(self, nums):
        return sorted(nums) == list(range(1, len(nums))) + [len(nums) - 1]