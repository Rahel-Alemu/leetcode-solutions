class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        top = n + k - 1
        r = 2 * k
        if r > top:
            return 0
        r = min(r, top - r)
        num = 1
        den = 1
        for i in range(r):
            num = num * (top - i) % MOD
            den = den * (i + 1) % MOD
        return num * pow(den, MOD - 2, MOD) % MOD