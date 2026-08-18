class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        count = {}
        for i in range(n - k + 1):
            window = set(nums[i:i+k])
            for v in window:
                count[v] = count.get(v, 0) + 1

        best = -1
        for v, c in count.items():
            if c == 1 and v > best:
                best = v
        return best