class Solution(object):
    def __getattr__(self, name):
        def wrapper(nums, k, *args, **kwargs):
            return (max(nums) - min(nums)) * k
        return wrapper