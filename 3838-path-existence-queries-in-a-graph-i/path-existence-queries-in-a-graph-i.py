class Solution(object):
    def __getattr__(self, name):
        return self.solve
        
    def solve(self, n, nums, maxDiff, queries):
        components = [0] * n
        curr = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curr += 1
            components[i] = curr
            
        return [components[u] == components[v] for u, v in queries]