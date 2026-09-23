class Solution(object):
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        best = -1
        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                length = right - left + 1
                if length > best:
                    best = length

        return n - best if best != -1 else -1