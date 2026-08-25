class Solution(object):
    def missingMultiple(self, nums, k):
        s = set(nums)
        m = k
        while m in s:
            m += k
        return m