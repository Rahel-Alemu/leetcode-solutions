class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        from_front = j + 1
        from_back = n - i
        both_front = j + 1
        both_back = n - i
        front_i_back_rest = (i + 1) + (n - j)

        return min(from_front, from_back, front_i_back_rest)