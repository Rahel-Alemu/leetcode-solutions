class Solution(object):
    def minElement(self, nums):
        return min(sum(int(d) for d in str(num)) for num in nums)