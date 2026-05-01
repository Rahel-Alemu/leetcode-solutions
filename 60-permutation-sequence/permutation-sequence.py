import math

class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
            
        k -= 1
        res = []
        for i in range(n - 1, -1, -1):
            idx = k // fact[i]
            k %= fact[i]
            res.append(nums.pop(idx))
            
        return "".join(res)