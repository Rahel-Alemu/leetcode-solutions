class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def upd(B, i, v):
            while i <= n + 1:
                B[i] += v
                i += i & -i

        def qry(B, i):
            s = 0
            while i > 0:
                s += B[i]
                i -= i & -i
            return s

        def range_add(l, r, v):  # 1-indexed inclusive
            upd(B1, l, v)
            upd(B1, r + 1, -v)
            upd(B2, l, v * (l - 1))
            upd(B2, r + 1, -v * r)

        def prefix_sum(i):
            return qry(B1, i) * i - qry(B2, i)

        last = {}
        cur = 0
        ans = 0
        for j in range(n):
            p = last.get(nums[j], -1)
            l, r = p + 2, j + 1  # 1-indexed positions for i in [p+1, j]
            L = j - p
            S = prefix_sum(r) - prefix_sum(l - 1)
            cur += 2 * S + L
            range_add(l, r, 1)
            last[nums[j]] = j
            ans = (ans + cur) % MOD
        return ans