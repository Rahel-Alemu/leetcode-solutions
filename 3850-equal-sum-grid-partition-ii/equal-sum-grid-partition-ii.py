import collections

class Solution:
    def canPartitionGrid(self, grid):
        m = len(grid)
        n = len(grid[0])
        total_sum = 0
        row_sums = [0] * m
        col_sums = [0] * n
        full_counts = collections.defaultdict(int)
        
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                total_sum += val
                row_sums[r] += val
                col_sums[c] += val
                full_counts[val] += 1

        # Horizontal Cuts
        s1 = 0
        top_counts = collections.defaultdict(int)
        bottom_counts = full_counts.copy()
        for i in range(m - 1):
            for c in range(n):
                v = grid[i][c]
                top_counts[v] += 1
                bottom_counts[v] -= 1
                if bottom_counts[v] == 0: del bottom_counts[v]
            
            s1 += row_sums[i]
            s2 = total_sum - s1
            
            if s1 == s2: return True
            
            # Discount from Top Section (s1)
            diff1 = s1 - s2
            if diff1 > 0:
                h, w = i + 1, n
                if h > 1 and w > 1:
                    if diff1 in top_counts: return True
                elif h == 1:
                    if grid[0][0] == diff1 or grid[0][n-1] == diff1: return True
                elif w == 1:
                    if grid[0][0] == diff1 or grid[i][0] == diff1: return True
            
            # Discount from Bottom Section (s2)
            diff2 = s2 - s1
            if diff2 > 0:
                h, w = m - 1 - i, n
                if h > 1 and w > 1:
                    if diff2 in bottom_counts: return True
                elif h == 1:
                    if grid[i+1][0] == diff2 or grid[i+1][n-1] == diff2: return True
                elif w == 1:
                    if grid[i+1][0] == diff2 or grid[m-1][0] == diff2: return True

        # Vertical Cuts
        s1 = 0
        left_counts = collections.defaultdict(int)
        right_counts = full_counts.copy()
        for j in range(n - 1):
            for r in range(m):
                v = grid[r][j]
                left_counts[v] += 1
                right_counts[v] -= 1
                if right_counts[v] == 0: del right_counts[v]
            
            s1 += col_sums[j]
            s2 = total_sum - s1
            
            if s1 == s2: return True
            
            # Discount from Left Section (s1)
            diff1 = s1 - s2
            if diff1 > 0:
                h, w = m, j + 1
                if h > 1 and w > 1:
                    if diff1 in left_counts: return True
                elif h == 1:
                    if grid[0][0] == diff1 or grid[0][j] == diff1: return True
                elif w == 1:
                    if grid[0][0] == diff1 or grid[m-1][0] == diff1: return True
                    
            # Discount from Right Section (s2)
            diff2 = s2 - s1
            if diff2 > 0:
                h, w = m, n - 1 - j
                if h > 1 and w > 1:
                    if diff2 in right_counts: return True
                elif h == 1:
                    if grid[0][j+1] == diff2 or grid[0][n-1] == diff2: return True
                elif w == 1:
                    if grid[0][j+1] == diff2 or grid[m-1][j+1] == diff2: return True
        
        return False