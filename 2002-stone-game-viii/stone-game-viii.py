class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        suf = [0] * (n + 1)
        suf[n] = prefix[n]
        for i in range(n - 1, 0, -1):
            fi = suf[i + 1]
            g = prefix[i] - fi
            suf[i] = max(g, suf[i + 1])

        return suf[2]
        