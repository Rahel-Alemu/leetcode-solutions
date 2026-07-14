class Solution(object):
    def subsequencePairCount(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        MOD = 10**9 + 7
        max_val = max(nums)
        
        g_table = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        for i in range(max_val + 1):
            for j in range(max_val + 1):
                g_table[i][j] = gcd(i, j)
                
        dp = {(0, 0): 1}
        
        for x in nums:
            new_dp = dict(dp)
            for (g1, g2), w in dp.items():
                ng1 = g_table[g1][x] if g1 else x
                k1 = (ng1, g2)
                new_dp[k1] = (new_dp.get(k1, 0) + w) % MOD
                
                ng2 = g_table[g2][x] if g2 else x
                k2 = (g1, ng2)
                new_dp[k2] = (new_dp.get(k2, 0) + w) % MOD
                
            dp = new_dp
            
        ans = 0
        for (g1, g2), w in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + w) % MOD
                
        return ans