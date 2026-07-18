class Solution(object):
    def __getattr__(self, name):
        def wrapper(nums):
            a = min(nums)
            b = max(nums)
            while b:
                a, b = b, a % b
            return a
        return wrapper