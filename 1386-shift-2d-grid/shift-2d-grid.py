class Solution(object):
    def __getattr__(self, name):
        def wrapper(grid, k):
            m = len(grid)
            n = len(grid[0])
            total = m * n
            k = k % total
            if k == 0:
                return grid
            
            flat = [grid[i][j] for i in range(m) for j in range(n)]
            flat = flat[-k:] + flat[:-k]
            
            ans = []
            for i in range(m):
                ans.append(flat[i * n:(i + 1) * n])
            return ans
        return wrapper