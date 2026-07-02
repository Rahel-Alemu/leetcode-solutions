from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        best = [[-1] * n for _ in range(m)]
        start = health - grid[0][0]

        if start <= 0:
            return False

        q = deque([(0, 0)])
        best[0][0] = start

        while q:
            x, y = q.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nh = best[x][y] - grid[nx][ny]
                    if nh > best[nx][ny] and nh > 0:
                        best[nx][ny] = nh
                        q.append((nx, ny))

        return False