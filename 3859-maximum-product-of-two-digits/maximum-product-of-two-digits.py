class Solution(object):
    def maxProduct(self, n):
        digits = [int(c) for c in str(n)]
        digits.sort()
        return digits[-1] * digits[-2]