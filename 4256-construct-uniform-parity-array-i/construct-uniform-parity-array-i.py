class Solution(object):
    def uniformArray(self, nums1):
        cnt0 = sum(1 for x in nums1 if x % 2 == 0)
        cnt1 = len(nums1) - cnt0

        t0_feasible = (cnt1 == 0 or cnt1 >= 2)
        t1_feasible = (cnt0 == 0 or cnt1 >= 1)

        return t0_feasible or t1_feasible