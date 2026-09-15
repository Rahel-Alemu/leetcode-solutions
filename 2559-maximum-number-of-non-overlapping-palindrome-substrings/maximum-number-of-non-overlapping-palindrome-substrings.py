class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n - 1):
            is_pal[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                is_pal[i][j] = (s[i] == s[j]) and is_pal[i + 1][j - 1]

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= k and is_pal[i - k][i - 1]:
                cand = 1 + dp[i - k]
                if cand > dp[i]:
                    dp[i] = cand
            if i >= k + 1 and is_pal[i - k - 1][i - 1]:
                cand = 1 + dp[i - k - 1]
                if cand > dp[i]:
                    dp[i] = cand

        return dp[n]