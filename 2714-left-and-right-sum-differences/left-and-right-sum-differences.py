class Solution(object):
    def leftRightDifference(self, nums):
        total = sum(nums)
        left_sum = 0
        ans = []
        for num in nums:
            total -= num
            ans.append(abs(left_sum - total))
            left_sum += num
        return ans