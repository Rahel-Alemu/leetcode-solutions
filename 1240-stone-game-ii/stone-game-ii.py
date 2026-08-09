class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if i == n:
                return 0
            if i + 2 * m >= n:
                return suffix[i]
            key = (i, m)
            if key in memo:
                return memo[key]
            best = 0
            for x in range(1, 2 * m + 1):
                best = max(best, suffix[i] - dp(i + x, max(m, x)))
            memo[key] = best
            return best

        return dp(0, 1)