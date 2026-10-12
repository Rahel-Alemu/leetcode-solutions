class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        cnt = [0] * 31
        for x in nums:
            for b in range(31):
                if (x >> b) & 1:
                    cnt[b] += 1

        total = 0
        for _ in range(k):
            val = 0
            for b in range(31):
                if cnt[b] > 0:
                    cnt[b] -= 1
                    val |= (1 << b)
            total = (total + val * val) % MOD
        return total