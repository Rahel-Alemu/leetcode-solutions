class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prev_mask = 1  # represents balance 0 before processing this cell
                else:
                    prev_mask = 0
                    if i > 0:
                        prev_mask |= dp[i - 1][j]
                    if j > 0:
                        prev_mask |= dp[i][j - 1]

                if prev_mask == 0:
                    dp[i][j] = 0
                    continue

                ch = grid[i][j]
                if ch == '(':
                    dp[i][j] = prev_mask << 1
                else:
                    dp[i][j] = prev_mask >> 1

        return (dp[m - 1][n - 1] & 1) != 0