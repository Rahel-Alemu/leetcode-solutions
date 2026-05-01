class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * v for i, v in enumerate(nums))
        max_f = f
        
        for i in range(1, n):
            f = f + total_sum - n * nums[n - i]
            if f > max_f:
                max_f = f
                
        return max_f