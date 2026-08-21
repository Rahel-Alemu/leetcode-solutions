class Solution(object):
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(coins)
        subsets = []
        for mask in range(1, 1 << n):
            l = 1
            cnt = 0
            for i in range(n):
                if mask & (1 << i):
                    l = l * coins[i] // gcd(l, coins[i])
                    cnt += 1
            sign = 1 if cnt % 2 == 1 else -1
            subsets.append((l, sign))

        def count(x):
            total = 0
            for l, sign in subsets:
                total += sign * (x // l)
            return total

        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo