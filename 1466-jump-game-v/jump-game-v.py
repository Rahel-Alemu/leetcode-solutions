class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [0] * n
        
        def dfs(i):
            if dp[i]:
                return dp[i]
            
            res = 1
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))
                
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))
                
            dp[i] = res
            return res
            
        return max(dfs(i) for i in range(n))