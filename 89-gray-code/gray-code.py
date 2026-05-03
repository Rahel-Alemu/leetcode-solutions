class Solution:
    def grayCode(self, n):
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res