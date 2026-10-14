class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        digits = '9' * q
        if r:
            digits += str(r)
        digits += '0' * (num - len(digits))
        return digits